# DesktopAppTemplate

Template PySide6 using plugins.


## Plugins

- DataPlugin
  ----------
  Wraps certain types of data, e.g., DICOM images, CT scans, CSV files, etc. It
  contains methods for accessing the data. For example, with CSV data you can 
  get the header and rows, as well as individual row items.

- LoaderPlugin
  ------------
  Loads certain types of data, e.g., DICOM images, CT scans, CSV files, etc.

- ProcessorPlugin
  ---------------
  Processes certain types of data, e.g., anonyize DICOM images
  
- ViewPlugin
  ----------
  Views certain things

All plugins, except data plugins, are associated with a view plugin that allows
the user to set their configuration before running them. So the CsvLoaderPlugin
requires a view plugin for specifying the CSV file path. Once the CSV data is 
loaded, it should be displayed as a table. That would be a TableView, not a plugin
because it's a general purpose object that can be reused everywhere. So is there
a difference between View and ViewPlugin objects? Why not make TableView a plugin
as well? This would keep it consistent with the rest. The table view plugin will
always be available in the basic installation.


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