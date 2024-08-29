import sys
import os
import pydicom
import numpy as np
import json
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QFileSystemModel, QVBoxLayout, QLabel, QMessageBox, QSizePolicy, QWidget, QProgressDialog, QPushButton
from PySide6.QtGui import QPixmap, QImage, QMouseEvent, QCursor
from PySide6.QtCore import Qt, QModelIndex, QPoint, QRect, QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ui_interface import Ui_MainWindow  # Bu, UI dosyanızdan oluşturulan sınıfı ifade eder
from Custom_Widgets import loadJsonStyle

class DicomImageView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Matplotlib için bir figür ve canvas oluştur
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Canvas'ı yerleştir
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)  # Kenar boşluklarını sıfıra ayarla
        layout.setSpacing(0)  # Boşlukları sıfırla
        self.setLayout(layout)

        # Boyut politikasını sabit boyut olarak ayarla
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setSizePolicy(size_policy)

    def resizeEvent(self, event):
        # Yeniden boyutlandırma olayını ele al
        new_size = event.size()
        self.canvas.setFixedSize(new_size)  # Canvas'ı QLabel boyutlarına eşitle
        self.figure.set_size_inches(new_size.width() / self.figure.get_dpi(), new_size.height() / self.figure.get_dpi())
        self.canvas.draw()

    def setDicomImage(self, image_array):
        # Eski içeriği temizle
        self.ax.clear()

        # Görüntüyü çerçevesiz olarak çiz
        self.ax.imshow(image_array, cmap='gray', aspect='auto')
        self.ax.set_position([0, 0, 1, 1])  # Eksenleri çerçevesiz hale getir
        self.ax.axis('off')  # Eksenleri kapat

        self.canvas.draw()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # DicomImageView widget'larını oluştur ve ilgili alanlara yerleştir
        self.dicom_views_main = [DicomImageView(self), DicomImageView(self)]
        self.dicom_views_sag = [DicomImageView(self), DicomImageView(self)]
        self.dicom_views_sol = [DicomImageView(self), DicomImageView(self)]

        layout_main = QVBoxLayout(self.ui.altLabel)
        layout_main_2 = QVBoxLayout(self.ui.altLabel_2)
        layout_sag = QVBoxLayout(self.ui.sagLabel)
        layout_sag_2 = QVBoxLayout(self.ui.sagLabel_2)
        layout_sol = QVBoxLayout(self.ui.solLabel)
        layout_sol_2 = QVBoxLayout(self.ui.solLabel_2)

        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main_2.setContentsMargins(0, 0, 0, 0)
        layout_sag.setContentsMargins(0, 0, 0, 0)
        layout_sag_2.setContentsMargins(0, 0, 0, 0)
        layout_sol.setContentsMargins(0, 0, 0, 0)
        layout_sol_2.setContentsMargins(0, 0, 0, 0)

        layout_main.setSpacing(0)
        layout_main_2.setSpacing(0)
        layout_sag.setSpacing(0)
        layout_sag_2.setSpacing(0)
        layout_sol.setSpacing(0)
        layout_sol_2.setSpacing(0)

        layout_main.addWidget(self.dicom_views_main[0])
        layout_main_2.addWidget(self.dicom_views_main[1])
        layout_sag.addWidget(self.dicom_views_sag[0])
        layout_sag_2.addWidget(self.dicom_views_sag[1])
        layout_sol.addWidget(self.dicom_views_sol[0])
        layout_sol_2.addWidget(self.dicom_views_sol[1])

        # Variables for window movement and resizing
        self._isDragging = False
        self._startPos = QPoint(0, 0)
        self._isResizing = False
        self._startRect = QRect()
        self._cursorChanged = False

        # Connect move window functionality
        self.ui.headerContainer.installEventFilter(self)

        # Load JSON style
        loadJsonStyle(self, self.ui)

        # Load window configuration from JSON
        self.load_window_configuration()

        self.show()

        # EXPAND CENTER MENU WIDGET 
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.fileBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        # CLOSE CENTER MENU WIDGET 
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET 
        self.ui.toolsBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.dataBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        # CLOSE RIGHT MENU WIDGET 
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificaitionContainer.collapseMenu())

        # Connect the open file and open folder buttons to their functions
        self.ui.fileBtn_2.clicked.connect(self.load_dicom_image)
        self.ui.folderBtn.clicked.connect(self.open_folder)

        # Setup the file system model for the fileTreeView
        self.setup_file_tree_view()

        # Yükleme ekranı fonksiyonunu ekleyin
        self.loading_dialog = None

        # İleri ve geri butonlarını oluştur ve işlevlerini bağla
        self.ui.prevBtn.clicked.connect(self.show_prev_image)
        self.ui.nextBtn.clicked.connect(self.show_next_image)

        # Sayfa geçişi butonları için sinyalleri bağla
        self.ui.pagesPrevBtn.clicked.connect(self.show_prev_page)
        self.ui.pagesNextBtn.clicked.connect(self.show_next_page)

    def show_loading_dialog(self, message, maximum):
        self.loading_dialog = QProgressDialog(message, None, 0, maximum, self)
        self.loading_dialog.setWindowTitle("Loading")
        self.loading_dialog.setWindowModality(Qt.WindowModal)
        self.loading_dialog.setMinimumDuration(0)
        self.loading_dialog.show()

    def load_window_configuration(self):
        # Load window configuration from JSON file
        json_file_path = os.path.join(os.path.dirname(__file__), 'style.json')
        try:
            with open(json_file_path, 'r') as f:
                config = json.load(f)
                main_window_config = config.get("QMainWindow", [])[0]
                if main_window_config.get("resizable", False):
                    self.setMouseTracking(True)
        except FileNotFoundError:
            QMessageBox.warning(self, "File Not Found", f"Could not find the configuration file: {json_file_path}")

    def eventFilter(self, obj, event):
        if obj == self.ui.headerContainer:
            if event.type() == QMouseEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self._isDragging = True
                    self._startPos = event.globalPos() - self.frameGeometry().topLeft()
                    event.accept()
            elif event.type() == QMouseEvent.MouseMove:
                if self._isDragging:
                    self.move(event.globalPos() - self._startPos)
                    event.accept()
            elif event.type() == QMouseEvent.MouseButtonRelease:
                if event.button() == Qt.LeftButton:
                    self._isDragging = False
                    event.accept()
        return super(MainWindow, self).eventFilter(obj, event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.is_near_edge(event.pos()):
                self._isResizing = True
                self._startPos = event.globalPos()
                self._startRect = self.frameGeometry()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._isResizing:
            delta = event.globalPos() - self._startPos
            new_rect = self._startRect.adjusted(0, 0, delta.x(), delta.y())
            self.setGeometry(new_rect)
            event.accept()
        elif self.is_near_edge(event.pos()):
            if not self._cursorChanged:
                self.setCursor(QCursor(Qt.SizeFDiagCursor))
                self._cursorChanged = True
        else:
            if self._cursorChanged:
                self.unsetCursor()
                self._cursorChanged = False

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isResizing = False
            event.accept()

    def is_near_edge(self, pos):
        margin = 10
        near_right = pos.x() > self.width() - margin
        near_bottom = pos.y() > self.height() - margin
        near_corner = near_right and near_bottom

        if near_corner:
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self.unsetCursor()
        
        return near_corner

    def load_dicom_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open DICOM File", "", "DICOM Files (*.dcm);;Images (*.png *.xpm *.jpg)")
        if file_name:
            self.display_images(file_name)
            # Update fileTreeView with the selected file's directory
            self.update_file_tree_view(os.path.dirname(file_name))

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", "")
        if folder_path:
            self.ui.fileTreeView.setRootIndex(self.model.index(folder_path))
            self.load_folder_images(folder_path)
            # Update fileTreeView with the selected folder
            self.update_file_tree_view(folder_path)

    def setup_file_tree_view(self):
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.ui.fileTreeView.setModel(self.model)
        self.ui.fileTreeView.setRootIndex(self.model.index(''))
        self.ui.fileTreeView.setColumnWidth(0, 250)
        self.ui.fileTreeView.clicked.connect(self.on_tree_view_clicked)

    def load_folder_images(self, folder_path):
        self.image_files = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg', '.dcm')):
                    self.image_files.append(os.path.normpath(os.path.join(root, file)))

        if self.image_files:
            self.images = []
            self.show_loading_dialog("Loading DICOM files...", len(self.image_files))
            for i, file in enumerate(self.image_files):
                dicom_file = pydicom.dcmread(file)
                self.images.append(dicom_file.pixel_array)
                self.loading_dialog.setValue(i + 1)
            
            self.images = np.array(self.images)
            self.loading_dialog.close()
            
            self.current_image_index = 0
            self.display_current_image()
            
            if len(self.image_files) > 1:
                self.ui.horizontalScrollBar.setMaximum(len(self.image_files) - 1)
                self.ui.horizontalScrollBar.valueChanged.connect(self.scrollbar_value_changed)
            else:
                self.ui.horizontalScrollBar.setMaximum(0)

    def display_current_image(self):
        file_path = self.image_files[self.current_image_index]
        image_array = self.images[self.current_image_index]
        self.display_images(file_path, image_array)
        self.update_tree_view_selection(file_path)
        self.update_image_info()

    def update_image_info(self):
        total_images = len(self.image_files)
        current_image_number = self.current_image_index + 1
        self.ui.label_8.setText(f"{current_image_number}/{total_images}")

    def scrollbar_value_changed(self, value):
        self.current_image_index = value
        self.display_current_image()

    def on_tree_view_clicked(self, index: QModelIndex):
        file_path = os.path.normpath(self.model.filePath(index))
        if os.path.isfile(file_path):
            if file_path in self.image_files:
                self.current_image_index = self.image_files.index(file_path)
                self.display_current_image()
                self.ui.horizontalScrollBar.setValue(self.current_image_index)
            else:
                print(f"{file_path} is not in image_files list")

    def update_tree_view_selection(self, file_path):
        index = self.model.index(file_path)
        self.ui.fileTreeView.setCurrentIndex(index)
        self.ui.fileTreeView.scrollTo(index)

    def update_file_tree_view(self, path):
        self.ui.fileTreeView.setRootIndex(self.model.index(path))

    def display_images(self, file_path, image_array=None):
        if image_array is None:
            dicom_image = pydicom.dcmread(file_path)
            if not hasattr(dicom_image, 'PixelData'):
                QMessageBox.warning(self, "DICOM Error", "Selected DICOM file does not contain valid pixel data.")
                return
            try:
                image_array = dicom_image.pixel_array
            except AttributeError:
                QMessageBox.warning(self, "DICOM Error", "Unable to convert the pixel data.")
                return

            if 'RescaleSlope' in dicom_image and 'RescaleIntercept' in dicom_image:
                slope = dicom_image.RescaleSlope
                intercept = dicom_image.RescaleIntercept
                image_array = image_array * slope + intercept

        for view in self.dicom_views_main:
            view.setDicomImage(image_array)

        if hasattr(self, 'images') and self.images.size > 0:
            # Coronal ve Sagittal görüntüleri oluştur
            coronal_images = np.transpose(self.images, (1, 0, 2))  # Reorient to (Height, Depth, Width)
            sagittal_images = np.transpose(self.images, (2, 0, 1))  # Reorient to (Width, Depth, Height)

            # Coronal ve Sagittal görüntülerin ortadaki dilimlerini göster
            coronal_index = self.images.shape[1] // 2
            sagittal_index = self.images.shape[2] // 2

            for view in self.dicom_views_sag:
                view.setDicomImage(coronal_images[coronal_index])
            
            for view in self.dicom_views_sol:
                view.setDicomImage(sagittal_images[sagittal_index])

    def show_prev_image(self):
        """Bir önceki resmi gösterir"""
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.display_current_image()
            self.ui.horizontalScrollBar.setValue(self.current_image_index)

    def show_next_image(self):
        """Bir sonraki resmi gösterir"""
        if self.current_image_index < len(self.image_files) - 1:
            self.current_image_index += 1
            self.display_current_image()
            self.ui.horizontalScrollBar.setValue(self.current_image_index)

    def show_prev_page(self):
        """Bir önceki sayfayı gösterir"""
        current_index = self.ui.mainPages.currentIndex()
        if current_index > 0:
            self.ui.mainPages.setCurrentIndex(current_index - 1)

    def show_next_page(self):
        """Bir sonraki sayfayı gösterir"""
        current_index = self.ui.mainPages.currentIndex()
        if current_index < self.ui.mainPages.count() - 1:
            self.ui.mainPages.setCurrentIndex(current_index + 1)

    def moveWindow(self, event=None):
        pass

    def toggleWindowSize(self, event=None):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
