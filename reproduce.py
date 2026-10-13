from pathlib import Path
import zipfile,tempfile,subprocess,sys
base=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as d:
    with zipfile.ZipFile(base/'research_data_and_code.zip') as z:
        for name in z.namelist():
            assert not Path(name).is_absolute() and '..' not in Path(name).parts
        z.extractall(d)
    subprocess.run([sys.executable,str(Path(d)/'code/recompute.py')],check=True)
    out=base/'recomputed.json'
    out.write_bytes((Path(d)/'recomputed/recomputed.json').read_bytes())
    print('Saved:',out)
