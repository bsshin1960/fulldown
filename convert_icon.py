import os
from PIL import Image

def convert_png_to_ico(png_path, ico_path):
    print(f"Opening PNG from: {png_path}")
    if not os.path.exists(png_path):
        print(f"Error: PNG file not found at {png_path}")
        return False
    
    img = Image.open(png_path)
    
    # Standard sizes for Windows ICO files
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    print(f"Saving multi-size ICO to: {ico_path}")
    img.save(ico_path, format='ICO', sizes=sizes)
    print("Conversion completed successfully!")
    return True

if __name__ == "__main__":
    png_source = r"C:\Users\SBS\.gemini\antigravity-ide\brain\352376aa-2f3c-4c4e-8707-c36126ec14ef\cursor_menu_app_icon_1782451310167.png"
    ico_dest = r"c:\Temp\Antigrvity\fulldown_menu\app_icon.ico"
    
    try:
        convert_png_to_ico(png_source, ico_dest)
    except ImportError:
        print("Pillow is not installed. Installing Pillow now...")
        import subprocess
        subprocess.check_call(["pip", "install", "Pillow"])
        # Retry import and conversion
        from PIL import Image
        convert_png_to_ico(png_source, ico_dest)
