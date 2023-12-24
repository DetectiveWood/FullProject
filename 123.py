import os
from PyQt5.QtCore import Qt, QUrl, QDirIterator, QDir,QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QApplication,QLabel, QWidget,QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog,QProgressBar,QGroupBox
from time import sleep
from random import randint
global music_files
global current_file_index
global media_player
current_file_index = 0
class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.music_files = [] # Список файлов с музыкой
        self.current_file_index = 0 # Текущий индекс файла

    def browse_music_files(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory', 'C:\\')
        music_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in ['.mp3', '.wav', '.flac', '.aac']:
                    music_files.append(os.path.join(root, file))
        self.music_files.extend(music_files)

    def play_music(self):
        if not self.music_files:
            return
        file = self.music_files[self.current_file_index]
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
        self.media_player.play()

    def stop_music(self):
        if not self.music_files:
            return
        self.media_player.stop()

    def skip_to_next(self):
        if not self.music_files:
            return
        if self.current_file_index < len(self.music_files) - 1:
            self.current_file_index += 1
        else:
            self.current_file_index = 0
        self.stop_music()
        self.play_music()
def Page_1():
    Start.hide()
    win.setStyleSheet("#MainWindow{border-image:url(list 3.png)""}")
    mp.show()
def Page_lern():
    Start.hide()
    win.setStyleSheet("#MainWindow{border-image:url(list 4.png)""}")
    dio.show()
def Page_lern_2():
    global music_files
    global current_file_index
    dio.hide()
    win.setStyleSheet("#MainWindow{border-image:url(list 2.png)""}")
    win.setGeometry(100, 100, 900, 500)
    win.setMinimumSize(900, 500)
    directory = QFileDialog.getExistingDirectory(win, 'Select Directory', 'E:\\')
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in ['.mp3', '.wav', '.flac', '.aac']:
                music_files.append(os.path.join(root, file))
    music_files.extend(music_files)
    Player.show()
def Page_mn():
    mp.hide()
    win.setStyleSheet("#MainWindow{border-image:url(list 2.png)""}")
    win.setGeometry(100, 100, 900, 500)
    win.setMinimumSize(900, 500)
    Player2.show()
def Page_agr():
    mp.hide()
    win.setStyleSheet("#MainWindow{border-image:url(list 2.png)""}")
    win.setGeometry(100, 100, 900, 500)
    win.setMinimumSize(900, 500)
    Player2.show()
def con():
    g = 0
    con_Prog.setValue(g)
    while g<100:
        sleep(0.3)
        g = g+randint(0,2)
        if g>100 or g==100:
            g =100
            con_res.setStyleSheet("""
                    #con_res_1{
                    border-image:url(brainbit on1.png);
                    }""")
            break
        con_Prog.setValue(g)
        win.update()
def Play_Rick():
    global music_files
    global current_file_index
    global media_player
    if not music_files:
        return
    file = music_files[current_file_index]
    media_player = QMediaPlayer()
    media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
    while True:
        media_player.play()
        g = randint(50,65)
        sleep(2)
        Prog_mnt.setValue(g)
        Prog_agr.setValue(100-g)
app = QApplication([])
Global_lay =QVBoxLayout()
# region
Start = QGroupBox()
Main_lay = QVBoxLayout()
Start.setObjectName("Start")
Start.setStyleSheet("""#Start{
                    background-color:transparent;
                    border: none;
                    }""")
Play_but = QPushButton()
Play_but.clicked.connect(Page_1)
lern_but = QPushButton()
lern_but.clicked.connect(Page_lern)
con_but = QPushButton()
con_but.clicked.connect(con)
con_but.clicked.connect(con)
con_res = QLabel()
Play_but.setObjectName("Play_bt_1")
con_but.setObjectName("con_but_1")
lern_but.setObjectName("lern_but_1")
con_res.setObjectName("con_res_1")
con_res.setStyleSheet("""
                    #con_res_1{
                    border-image:url(brainbit off1.png);
                        }    
                    """)
con_but.setStyleSheet("""
                    #con_but_1{
                    border-image:url(conect1.png);
                        }    
                    """)
lern_but.setStyleSheet("""
                        #lern_but_1{
                        border-image:url(uch1.png);
                        border:1px;
                        }
                        """)
Play_but.setStyleSheet("""
                        #Play_bt_1{
                        border-image:url(play1.png);
                        border:1px;
                        }
                        """)
con_but.setMaximumSize(300,300)
con_Prog = QProgressBar()
con_Prog.setObjectName("Prg_bar")

con_Prog.setStyleSheet("""
                       #Prg_bar{
                       background-color: transparent;
                       border:1px;
                       }
                       #Prg_bar::chunk{
                       color: rgb(255,255,255);
                       background-color:rgb(255,147,125)
                       }
""")
con_res.setMaximumSize(300,300)
Play_but.setMinimumSize(110,0)
Play_but.setMaximumSize(145,300)
lern_but.setMaximumSize(900,900)
Sv = QVBoxLayout()
Sv.setSpacing(12)
Sv.addStretch(1)
Sh_4 = QHBoxLayout()
Sh_2 = QHBoxLayout()
Sh_3 = QHBoxLayout()
Sh_2.setSpacing(20)
Sh_3.setSpacing(18)
Sh_2.addStretch(3)
Sh_2.addWidget(Play_but,stretch=1)
Sh_2.addStretch(3)
Sv.addStretch(9)
Sv.addLayout(Sh_2,stretch=4)
Sh_3.addStretch(5)
Sh_3.addWidget(lern_but,stretch=8)
Sh_3.addStretch(5)
Sh_4.setSpacing(6)
Sh_4.addWidget(con_but,stretch=2)
Sh_4.addWidget(con_Prog,stretch=2)
Sh_4.addWidget(con_res,stretch=2)
Sv.addLayout(Sh_3,stretch=3)
Sv.addLayout(Sh_4,stretch=3)
Sh = QHBoxLayout()
Main_lay.addLayout(Sv)
Start.setLayout(Main_lay)
Global_lay.addWidget(Start)
# endregion
#region
mp = QGroupBox()
mp.setObjectName("group_vibor")
mp.setStyleSheet("""
                #group_vibor{
                border:none;
                    }""")
Main_lay = QHBoxLayout()
But_ment = QPushButton()
But_ment.clicked.connect(Page_mn)
But_ctulhu = QPushButton()
But_ctulhu.clicked.connect(Page_agr)
But_ment.setMaximumSize(400,300)
But_ctulhu.setMaximumSize(400,300)
But_ment.setObjectName("but_ment_1")
But_ctulhu.setObjectName("but_agr_1")
But_ment.setStyleSheet("""
                        #but_ment_1{
                            border-image:url(knop1.png);
                            }""")
But_ctulhu.setStyleSheet("""
                        #but_agr_1{
                            border-image:url(knop 22.png);
                            }""")
qv = QVBoxLayout()
qv.setSpacing(10)
qv.addStretch(10)
qv.addWidget(But_ment,stretch=3)
qv.addWidget(But_ctulhu,stretch=3)
qv.addStretch(4)
Main_lay.addLayout(qv)
mp.setLayout(Main_lay)
Global_lay.addWidget(mp)
mp.hide()
# endregion
#region
dio =QGroupBox()
dio.setObjectName("dio")
dio.setStyleSheet("""
                    #dio{
                    border:none;
                        }""")
Main_lay = QVBoxLayout()
qh = QHBoxLayout()
dia_bt = QPushButton()
dia_bt.clicked.connect(Page_lern_2) #123
dia_bt.setObjectName("dio_bt")
dia_bt.setMaximumSize(3000,3000)
dia_bt.setStyleSheet("""
                    #dio_bt{
                    border-image:url(button 44.png)
                        }""")
qh.setSpacing(128)
qh.addStretch(49)
qh.addWidget(dia_bt,stretch=43)
qh.addStretch(1)
Main_lay.setSpacing(28)
Main_lay.addStretch(11)
Main_lay.addLayout(qh,stretch=4)
Main_lay.addStretch(13)
dio.setLayout(Main_lay)
Global_lay.addWidget(dio)
dio.hide()
#endregion
#region
Player = QGroupBox()
Player.setObjectName("Player_3")
Player.setStyleSheet("""
                    #Player_3{
                    border:none;
                    }
                    """)
Play_but_2 = QPushButton()
Play_but_2.clicked.connect(Play_Rick)
Play_but_2.setMaximumSize(9000,9000)
Play_but_2.setObjectName("Play_bt_2")
Play_but_2.setStyleSheet("""
                            #Play_bt_2{
                            border-image:url(play1.png);
                            }""")
Prog_mnt = QProgressBar()
Prog_mnt.setMaximumSize(9000,9000)
Prog_mnt.setValue(100)
Prog_mnt.setObjectName("progira")
Prog_mnt.setStyleSheet("""
                        #progira{
                        background-color: transparent;
                        border:1px
                        }
                        #progira::chunk 
                        {
                        background: rgb(255,147,125);
                        }
                        """)
Prog_agr = QProgressBar()
Prog_agr.setMaximumSize(9000,9000)
Prog_agr.setObjectName("Prog_agr_2")
Prog_agr.setValue(100)
Prog_agr.setStyleSheet("""
                        #Prog_agr_2{
                        background-color: transparent;
                        border:1px;
                        }
                        #Prog_agr_2::chunk 
                        {
                        background: rgb(180,125,249);
                        }
                        """)
#255,147,125 180,125,249

Mp_name = QLabel()
fint = QFont()
fint.setPixelSize(35)
Mp_name.setObjectName("text_2")
Mp_name.setText("Rickroll")
Mp_name.setFont(fint)
Mp_name.setStyleSheet("""
                      #text_2{
                      color: rgb(255,255,255);
                      }
""")
album = QLabel()
album.setMaximumSize(3000, 3000)
album.setObjectName("album_img")
album.setStyleSheet("""
                    #album_img{
                    border-image:url(pust.png)
                    }
""")
But_next = QPushButton()
But_next.setObjectName("Next")
But_next.setMaximumSize(9000,9000)
But_next.setStyleSheet("""
                      #Next{
                      border-image:url(strel prav1.png);
                      }""")
But_lev = QPushButton()
But_lev.setObjectName("Lev")
But_lev.setMaximumSize(9000,9000)
But_lev.setStyleSheet("""
                      #Lev{
                      border-image:url(strel lev1.png);
                      }""")
Main_lay= QVBoxLayout()

qh_1= QHBoxLayout()
qh_2= QHBoxLayout()
qh_3= QHBoxLayout()
qh_4 = QHBoxLayout()
qh_5 = QHBoxLayout()
qh_1.setSpacing(10)
qh_2.setSpacing(10)
qh_1.addStretch(2)
qh_2.addStretch(2)
qh_1.addWidget(Prog_mnt,stretch=7)
qh_2.addWidget(Prog_agr,stretch=7)
qh_1.addStretch(1)
qh_2.addStretch(1)
qh_3.setSpacing(10)
qh_3.addStretch(4)
qh_3.addWidget(Mp_name,stretch=5)
qh_3.addStretch(1)
qhv= QVBoxLayout()
qhh = QHBoxLayout()
qh_4.setSpacing(100)
qh_4.addStretch(3)
qh_4.addWidget(album,stretch=10)
qh_4.addStretch(4)
qhv.setSpacing(10)
qhh.setSpacing(21)
qhv.addWidget(Mp_name,stretch=1)
qhh.addWidget(But_lev,stretch=7)
qhh.addWidget(Play_but_2,stretch=7)
qhh.addWidget(But_next,stretch=7)

qhv.addStretch(7)
qhv.addLayout(qhh,stretch=9)
qh_4.addLayout(qhv,stretch=14)
qh_4.addStretch(5)
Main_lay.setSpacing(12)
Main_lay.addStretch(2)
Main_lay.addLayout(qh_1,stretch=1)
Main_lay.addStretch(1)
Main_lay.addLayout(qh_2,stretch=2)
Main_lay.addStretch(4)
Main_lay.addLayout(qh_3,stretch=1)
Main_lay.addStretch(1)
Main_lay.addLayout(qh_4,stretch=30)
Main_lay.addStretch(21)
Player.setLayout(Main_lay)
Global_lay.addWidget(Player)
Player.hide()
#endregion
#region
Player2 = QGroupBox()
#Player2.setObjectName("Player_3")
#Player2.setStyleSheet("""
#                    #Player_3{
#                    border:none;
#                    }
#                    """)
Play_but_2 = QPushButton()
Play_but_2.setMaximumSize(9000,9000)
Play_but_2.setObjectName("Play_bt_2")
Play_but_2.clicked.connect(Play_Rick)
Play_but_2.setStyleSheet("""
                            #Play_bt_2{
                            border-image:url(play1.png);
                            }""")

Mp_name = QLabel()
fint = QFont()
fint.setPixelSize(35)
Mp_name.setObjectName("text_2")
Mp_name.setText("Rickroll")
Mp_name.setFont(fint)
Mp_name.setStyleSheet("""
                      #text_2{
                      color: rgb(255,255,255);
                      }
""")
album = QLabel()
album.setMaximumSize(360,360)
album.setObjectName("album_img")
album.setStyleSheet("""
                    #album_img{
                    border-image:url(pust.png);
                    border-radius:50;
                    }
""")
But_next = QPushButton()
But_next.setObjectName("Next")
But_next.setMaximumSize(9000,9000)
But_next.setStyleSheet("""
                      #Next{
                      border-image:url(strel prav1.png);
                      }""")
But_lev = QPushButton()
But_lev.setObjectName("Lev")
But_lev.setMaximumSize(9000,9000)
But_lev.setStyleSheet("""
                      #Lev{
                      border-image:url(strel lev1.png);
                      }""")
Main_lay= QVBoxLayout()

qh_1= QHBoxLayout()
qh_2= QHBoxLayout()
qh_3= QHBoxLayout()
qh_4 = QHBoxLayout()
qh_5 = QHBoxLayout()
qh_1.setSpacing(10)
qh_2.setSpacing(10)
qh_1.addStretch(2)
qh_2.addStretch(2)
qh_1.addStretch(7)
qh_2.addStretch(7)
qh_1.addStretch(1)
qh_2.addStretch(1)
qh_3.setSpacing(10)
qh_3.addStretch(4)
qh_3.addStretch(1)
qhv= QVBoxLayout()
qhh = QHBoxLayout()
qh_4.setSpacing(100)
qh_4.addStretch(3)
qh_4.addWidget(album,stretch=10)
qh_4.addStretch(4)
qhv.setSpacing(10)
qhh.setSpacing(21)
qhv.addWidget(Mp_name,stretch=1)
qhh.addWidget(But_lev,stretch=7)
qhh.addWidget(Play_but_2,stretch=7)
qhh.addWidget(But_next,stretch=7)

qhv.addStretch(5)
qhv.addLayout(qhh,stretch=5)

qh_4.addLayout(qhv,stretch=14)
qh_4.addStretch(5)
Main_lay.setSpacing(10)
Main_lay.addLayout(qh_1,stretch=1)
Main_lay.addLayout(qh_2,stretch=1)
Main_lay.addStretch(6)
Main_lay.addLayout(qh_3,stretch=1)
Main_lay.addStretch(5)
Main_lay.addLayout(qh_4,stretch=25)
Main_lay.addStretch(14)
Player2.setLayout(Main_lay)
Global_lay.addWidget(Player2)
Player2.hide()
#endregion
win = QWidget()
win.setLayout(Global_lay)
win.setObjectName("MainWindow")
win.setStyleSheet("#MainWindow{border-image:url(fon.png)""}")
win.setGeometry(100,100,700,500)
win.setMinimumSize(700,500)
win.show()
app.exec()