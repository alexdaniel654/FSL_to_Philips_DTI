# -*- mode: python ; coding: utf-8 -*-
import gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')
custom_images = Tree('D:\\ppxad2\\ownCloud\\University\\Renal Imaging\\Nephrectomy\\FSL_to_Philips_DTI\\icons', prefix='icons')
block_cipher = None


a = Analysis(['D:/ppxad2/ownCloud/University/Renal Imaging/Nephrectomy/FSL_to_Philips_DTI/fsl_gps_2_philips_bvecs.py'],
             pathex=['D:\\ppxad2\\ownCloud\\University\\Renal Imaging\\Nephrectomy\\FSL_to_Philips_DTI'],
             binaries=[],
             datas=[('Raw_Vectors\*.txt', 'Raw_Vectors')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('icon.ico', 'D:\\ppxad2\\ownCloud\\University\\Renal Imaging\\Nephrectomy\\FSL_to_Philips_DTI\\icons\\program_icon.ico', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          gooey_images,
          custom_images,
          [],
          name='fsl_spherical_dti_gen',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True,
          icon=os.path.join('icons','program_icon.ico'))
