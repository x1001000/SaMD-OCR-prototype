import streamlit as st
import pypdfium2 as pdfium
import pytesseract
import re

st.header('EyeSeeCam PDFs')
files = st.file_uploader(' ', type=['pdf'], accept_multiple_files=True, label_visibility='collapsed', key='EyeSeeCam')
for file in files:
    st.subheader(file.name)
    pdf = pdfium.PdfDocument(file)
    text = pdf[0].get_textpage().get_text_range()
    VNG = re.search('±(.*)±', text)
    if VNG:
        Mean = VNG.group(1).split()[1]
        Mean
    else:
        left, right = re.findall('60 ms : (.*) ±', text)
        right
        left
        Gain_Asymmetry = re.search('(.*%)', text).group(1)
        Gain_Asymmetry

st.header('ICS Impulse PDFs')
files = st.file_uploader(' ', type=['pdf'], accept_multiple_files=True, label_visibility='collapsed', key='ICS Impulse')
for file in files:
    st.subheader(file.name)
    pdf = pdfium.PdfDocument(file)
    bitmap = pdf[0].render(scale=10)
    pil_image = bitmap.to_pil().crop([50, 0, 5900, 2000])
    print(pil_image.size)
    st.image(pil_image)
    text = pytesseract.image_to_string(pil_image)
    print(text)
    Left = re.search('Left: (.*),', text).group(1).split(',')[0]
    Left
    Right = re.search('Right: (.*),', text).group(1).split(',')[0]
    Right
    Relative_Asymmetry = re.search('Relative Asymmetry: (.*%)', text).group(1)
    Relative_Asymmetry

st.header('Ecleris PDFs')
files = st.file_uploader(' ', type=['pdf'], accept_multiple_files=True, label_visibility='collapsed', key='Ecleris')
for file in files:
    st.subheader(file.name)
    pdf = pdfium.PdfDocument(file)

    st.write('Spontaneous:')
    bitmap = pdf[0].render(scale=10)
    pil_image = bitmap.to_pil()
    st.image(pil_image.crop([1800, 2900, 4000, 3200]))
    text = pytesseract.image_to_string(pil_image.crop([1800, 2900, 4000, 3200]))
    st.write(text.split()[-1].replace('O', '0'))
    text = pytesseract.image_to_string(pil_image.crop([2400, 2900, 4000, 3200]))
    st.write(text.split()[-1].replace('O', '0'))

    st.divider()
    st.write('Saccades:')
    bitmap = pdf[0].render(scale=10)
    pil_image = bitmap.to_pil().crop([1300, 6600, 4800, 7100])
    st.image(pil_image)
    text = pytesseract.image_to_string(pil_image)
    print(text)
    Leftward = re.search('Leftward(.*)\n', text).group(0)
    Leftward.split()[2]
    Rightward = re.search('Rightward(.*)\n', text).group(0)
    Rightward.split()[2]

    st.divider()
    st.write('Smooth:')
    bitmap = pdf[1].render(scale=10)
    pil_image = bitmap.to_pil().crop([500, 3600, 5000, 4300])
    st.image(pil_image)
    text = pytesseract.image_to_string(pil_image)
    print(text)
    Gain = re.search('Gain\n(.*)\n', text).group(1)
    Gain

    st.divider()
    st.write('Gaze:')
    bitmap = pdf[2].render(scale=10)
    pil_image = bitmap.to_pil()
    st.image(pil_image.crop([1200, 2600, 4500, 4000]))
    text = pytesseract.image_to_string(pil_image)
    print(text)
    groups = re.search('Dir\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n', text).groups()
    st.write(groups[1].replace('O', '0'))
    st.write(groups[3].replace('O', '0'))
    st.write(groups[5].replace('O', '0'))
    st.write(groups[7].replace('O', '0'))
