# DesktopAppTemplate

Template PySide6 using plugins.


## Plugins

- DataPlugin
  Wraps certain types of data, e.g., DICOM images, CT scans, CSV files, etc.

- LoaderPlugin
  Loads certain types of data, e.g., DICOM images, CT scans, CSV files, etc.

- ProcessorPlugin
  Processes certain types of data, e.g., anonyize DICOM images

- ViewPlugin
  Views certain things


## User scenarios

Let's say a user wishes to load a CSV file, run some statistics on it and visualize 
the results. What would be needed to do that? First of all, we need a CsvDataPlugin
to capture CSV data. The CsvLoaderPlugin knows how to load a CSV file (e.g., using 
Pandas). If the CsvLoaderPlugin is available (detected), a new menu item should be
available in the main window that allows the user to load CSV data. When the menu
item is clicked, a dialog window appears where the user can specify the file path of
the CSV data. Once the CSV data is loaded, it should be made available to the app
in a centralized manner. How? For this we need a data model hierarchy. Perhaps a
singleton DataManager?