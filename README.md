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


## Thoughts

How should I use plugins? There can be plugins for everything but then it becomes
very cumbersome to keep them in sync and let them interact with each other. Think
of plugins as larger system modules. Take the Mosamatic Desktop application: what
modules can you think of? Loading and analyzing CSV data could be one such module.
It contains everything to load CSV data, process it and visualize it. That would
be a single plugin. Or not? Same for Excel data. Actually, Excel and CSV could be
part of the same plugin. It's just tabular data (with support for multiple file
extensions, e.g., SPSS data). These plugins can be mirrored in the core and UI.
If you look at Mosamatic Desktop, we can envision plugins for different tasks, e.g.,
an DicomImagePlugin (as opposed to TablePlugin). The DicomImagePlugin allows loading of 
individual DICOM images as well as complete scans. The DicomImageAnonymizationPlugin
allows anonymization of DICOM images.

Should I use a plugin-based system? How often are you going to need it? You're
argument is that you want to offer the tool for free but may ask people to give
you money for developing custom plugins. A plugin in that sense should be independent
and work without any interference from other plugins. 