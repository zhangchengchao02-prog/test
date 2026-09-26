import zipfile, re, os

path = r'd:\zcc_code\code\test\Revised Manuscript (clean for typesetting).docx'
outdir = r'd:\zcc_code\code\test\paper_assets'
os.makedirs(outdir, exist_ok=True)
z = zipfile.ZipFile(path)
for i in z.infolist():
    if i.filename.startswith('word/media/') and i.file_size > 0:
        open(os.path.join(outdir, os.path.basename(i.filename)), 'wb').write(z.read(i.filename))

# report every drawing reference order in document.xml
xml = z.read('word/document.xml').decode('utf-8')
rels = z.read('word/_rels/document.xml.rels').decode('utf-8')
relmap = dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"', rels))
for m in re.finditer(r'(r:embed|r:id)="([^"]+)"', xml):
    t = relmap.get(m.group(2), '?')
    if 'media' in t:
        print(m.start(), m.group(1), t)
