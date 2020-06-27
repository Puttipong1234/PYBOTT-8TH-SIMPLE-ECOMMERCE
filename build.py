import sys
from cx_Freeze import setup, Executable

company_name = 'PYBOTT'
product_name = 'PYBOTT BASIC _ ECOMMERCE'

bdist_msi_options = {
    'upgrade_code': '{Banana-rama-30403344939493}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    }

path = sys.path
build_exe_options = {
"path": path,}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
exe = Executable(script='product_app.py',
                 base=base,
                )

setup(  name = "PYBOTT-MERCHANT",
        version = "1.1",
        description = "INVENTORY MANAGEMENT SYSTEM FOR PYBOTT-8TH",
        executables = [exe],
        options = {'bdist_msi': bdist_msi_options})