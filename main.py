"""Main entry point for To-Do List Pro desktop application."""
import sys
import os
import traceback
import tkinter as tk
from tkinter import messagebox

# Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def enable_high_dpi_awareness():
    """Enable High DPI awareness on Windows for sharp fonts."""
    if sys.platform == "win32":
        try:
            import ctypes
            # Shcore SetProcessDpiAwareness: 1 = Process_System_DPI_Aware, 2 = Process_Per_Monitor_DPI_Aware
            try:
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
            except Exception:
                ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

def main():
    enable_high_dpi_awareness()

    try:
        from app.database import Database
        from app.ui.theme import setup_styles
        from app.ui.main_window import MainWindow

        # Initialize SQLite database
        db = Database()

        # Create and run Main Window
        app = MainWindow(db)
        setup_styles()
        app.mainloop()

    except Exception as e:
        err_msg = traceback.format_exc()
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Khởi động thất bại", f"Đã xảy ra lỗi khi khởi động ứng dụng:\n\n{err_msg}")
        except Exception:
            print(f"Error starting application:\n{err_msg}", file=sys.stderr)

if __name__ == "__main__":
    main()
