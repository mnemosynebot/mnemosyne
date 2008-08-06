##############################################################################
#
# generic_card_widget.py <Peter.Bienstman@UGent.be>
#
##############################################################################

import gettext
_ = gettext.gettext

from PyQt4.QtCore import *
from PyQt4.QtGui import *



##############################################################################
#
# GenericCardWdgt
#
##############################################################################

class GenericCardWdgt(QWidget):
    
    ##########################################################################
    #
    # __init__
    #
    ##########################################################################
    
    def __init__(self, card_type, parent=None):
        
        QWidget.__init__(self, parent)

        self.card_type = card_type

        self.hboxlayout = QHBoxLayout(self)
        self.hboxlayout.setMargin(0)
        self.vboxlayout = QVBoxLayout()

        self.edit_boxes = {}

        for fact_key, fact_key_name in self.card_type.fields:
            
            self.vboxlayout.addWidget(QLabel(fact_key_name + ":", self))
            
            t = QTextEdit(self)
            t.setTabChangesFocus(True)
            t.setUndoRedoEnabled(True)
            t.setReadOnly(False)
            if len(self.card_type.fields) > 2:
                t.setMinimumSize(QSize(0,60))
            else:
                t.setMinimumSize(QSize(0,106))                
            self.vboxlayout.addWidget(t)
            self.edit_boxes[t] = fact_key
            
        self.hboxlayout.addLayout(self.vboxlayout)

        self.resize(QSize(QRect(0,0,325,264).size()).\
                    expandedTo(self.minimumSizeHint()))
        


        
    ##########################################################################
    #
    # get_data
    #
    ##########################################################################
    
    def get_data(self):

        # Get the data from the form.

        fact = {}
        for edit_box, fact_key in self.edit_boxes.iteritems():
            fact[fact_key] = unicode(edit_box.document().toPlainText())

        # TODO: Check if sufficient data is present.


        # Return the data.
        
        return fact 



    ##########################################################################
    #
    # clear
    #
    ##########################################################################
    
    def clear(self):

        for edit_box in self.edit_boxes:
            edit_box.setText("")
