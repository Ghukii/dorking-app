import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QLabel, QLineEdit, QTextEdit, QComboBox
from PyQt5 import uic

def setDefaultLanguage():
    file = open('logs/language.txt', 'w')
    file.write("English")
    file.close()

def get_language():
    file = open('logs/language.txt', 'r')
    lang = file.read()
    file.close()

    return lang

def get_theme():
    file = open('logs/theme.txt', 'r')
    theme = file.read()
    file.close()

    return theme

def get_css(theme):
    with open(f'styles/style_{theme}.css', 'r') as f:
        css = f.read()
    f.close()

    return css

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/gui.ui', self)

        self.label_tag = self.findChild(QLabel, 'label_tag')
        self.label_phrase = self.findChild(QLabel, 'label_phrase')
        self.label_site = self.findChild(QLabel, 'label_site')
        self.label_link = self.findChild(QLabel, 'label_link')
        self.label_inurl = self.findChild(QLabel, 'label_inurl')
        self.label_cache = self.findChild(QLabel, 'label_cache')
        self.label_related = self.findChild(QLabel, 'label_related')
        self.label_filetype = self.findChild(QLabel, 'label_filetype')

        self.tag_line = self.findChild(QLineEdit, 'tag_line')
        self.phrase_line = self.findChild(QLineEdit, 'phrase_line')
        self.site_line = self.findChild(QLineEdit, 'site_line')
        self.link_line = self.findChild(QLineEdit, 'link_line')
        self.inurl_line = self.findChild(QLineEdit, 'inurl_line')
        self.cache_line = self.findChild(QLineEdit, 'cache_line')
        self.related_line = self.findChild(QLineEdit, 'related_line')
        self.filetype_line = self.findChild(QLineEdit, 'filetype_line')

        self.languageBox = self.findChild(QComboBox, 'language')
        
        self.generate = self.findChild(QPushButton, 'generate')
        self.themeButton = self.findChild(QPushButton, 'theme')
        self.requestButton = self.findChild(QPushButton, 'request')

        self.output = self.findChild(QTextEdit, 'request_output')

        self.themeButton.setText(get_theme())

        setDefaultLanguage()
        self.setLanguage()

        self.generate.clicked.connect(self.generate_request)
        self.themeButton.clicked.connect(self.change_theme)
        self.requestButton.clicked.connect(self.browse)

        self.languageBox.currentIndexChanged.connect(self.setLanguageWithLog)

    def browse():
        pass

    def setLanguageWithLog(self):

        file = open('logs/language.txt', 'w')
        file.write(self.languageBox.currentText())
        file.close()

        self.language = self.languageBox.currentText()

        self.setLanguage()

    def setLanguage(self):
        file = open('logs/language.txt', 'r')
        lang = file.read()
        file.close()

        if lang == "Русский":
            self.label_tag.setText('Тэг')
            self.label_phrase.setText('Конкретная фраза')
            self.label_site.setText('Конкретный сайт')
            self.label_link.setText('Ссылка')
            self.label_inurl.setText('В url')
            self.label_cache.setText('Кэшированная версия')
            self.label_related.setText('Связанные сайты')
            self.label_filetype.setText('Файл')
            self.generate.setText('Сгенерировать')
            if get_theme() == 'dark':
                self.themeButton.setText('Темная')
            else:
                self.themeButton.setText('Светлая')

        elif lang == "English":
            self.label_tag.setText('Tag')
            self.label_phrase.setText('Certain phrase')
            self.label_site.setText('Certain site')
            self.label_link.setText('Link')
            self.label_inurl.setText('In url')
            self.label_cache.setText('Cached version')
            self.label_related.setText('Related sites')
            self.label_filetype.setText('File')
            self.generate.setText('Generate')
            self.themeButton.setText(get_theme())
        
        
    def change_theme(self):
        theme = get_theme()
        file = open('logs/theme.txt', 'w')

        if theme == 'dark':    
            file.write('light')
        else:
            file.write('dark')

        file.close()

        self.setLanguage()

        app.setStyleSheet(get_css(get_theme()))

    def generate_request(self):
        request = ''
        if self.tag_line.text():
            request += '@' + self.tag_line.text() + ' '
        if self.phrase_line.text():
            request += '"' + self.phrase_line.text() + '" '
        if self.site_line.text():
            request += 'site:' + self.site_line.text() + ' '
        if self.link_line.text():
            request += 'link:' + self.link_line.text() + ' '
        if self.inurl_line.text():
            request += 'inurl:' + self.inurl_line.text() + ' '
        if self.cache_line.text():
            request += 'cache:' + self.cache_line.text() + ' '
        if self.related_line.text():
            request += 'related:' + self.related_line.text() + ' '
        if self.filetype_line.text():
            request += 'filetype:' + self.filetype_line.text() + ' '

        self.output.setText(request)

        


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        theme = get_theme()

        css = get_css(theme)
        
        app.setStyleSheet(css)
        gui = GUI()
        gui.show()
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    