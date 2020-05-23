import sys

from PyQt5 import QtWidgets
from gui_2 import Ui_MainWindow
import qtmodern.styles
import qtmodern.windows
import matplotlib.pyplot as plt
import db_service
import datetime
from matplotlib.text import Text
from matplotlib.lines import Line2D
import gun_events


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.connection = db_service.create_connection(
            "guns_db.sqlite")  # Main variable for accessing conenction to the database

        self.all_plots_dict = dict()
        self.main_record_event_list = []  # collects all red circle events on line plot

        self.add_new_record_btn.clicked.connect(self.button_clicked_add_new_record)
        self.copy_shots_btn.clicked.connect(self.button_clicked_copy_shots)
        self.set_ui()

        self.create_bar_total_shots()
        self.create_bar_airline_shots()
        self.create_bar_tbs_shots()
        self.create_bar_solenoids_shots()
        self.create_line_plot()

    def set_ui(self):
        """
        Populates comboboxes and other ui elements from the database
        :return:
        """
        self.dateAndTimeDateTimeEdit.setDateTime(datetime.datetime.now())
        airline_types = db_service.return_airline_types(self.connection)

        for each in self.list_of_airline_type_comboxes():
            each.addItems(airline_types)

    def list_of_airline_type_comboxes(self):
        """
        Convenient container for all UI comboboxes for airline type comboboxes
        :return: list of QComboBoxes
        """
        airline_comboxes = [
            self.airline1TypeComboBox,
            self.airline2TypeComboBox,
            self.airline3TypeComboBox,
            self.airline4TypeComboBox,
            self.airline5TypeComboBox,
            self.airline6TypeComboBox,
            self.airlineForMSGComboBox
        ]
        return airline_comboxes

    def list_of_tb_spinners(self):
        """
        Convenient container for all UI spinners for TBs total count
        :return: list of QtSpinBoxes
        """
        tb_spinboxes = [
            self.tb1TotalShotsSpinBox,
            self.tb2TotalShotsSpinBox,
            self.tb3TotalShotsSpinBox,
            self.tb4TotalShotsSpinBox,
            self.tb5TotalShotsSpinBox,
            self.tb6TotalShotsSpinBox,
            self.msg_tb_TotalShotsSpinBox
        ]
        return tb_spinboxes

    def list_of_sol_spinners(self):
        """
        Convenient container for all UI spinners for SOLs total count
        :return: list of QtSpinBoxes
        """
        sol_spinners = [
            self.sol1TotalShotsSpinBox,
            self.sol2TotalShotsSpinBox,
            self.sol3TotalShotsSpinBox,
            self.sol4TotalShotsSpinBox,
            self.sol5TotalShotsSpinBox,
            self.sol6TotalShotsSpinBox,
            self.msg_sol_TotalShotsSpinBox
        ]
        return sol_spinners

    def list_of_gun_spinners(self):
        """
        Convenient container for all UI spinners for Guns total count
        :return: list of QtSpinBoxes
        """
        list_of_gun_spinners = [
            self.gun1TotalShotsSpinBox,
            self.gun2TotalShotsSpinBox,
            self.gun3TotalShotsSpinBox,
            self.gun4TotalShotsSpinBox,
            self.gun5TotalShotsSpinBox,
            self.gun6TotalShotsSpinBox,
            self.mSGTotalShotsSpinBox
        ]
        return list_of_gun_spinners

    def list_of_airline_spinners(self):
        """
        Convenient container for all UI spinners for Airlines total count
        :return: list of QtSpinBoxes
        """
        list_of_airline_spinners = [
            self.airline1TotalShotsSpinBox,
            self.airline2TotalShotsSpinBox,
            self.airline3TotalShotsSpinBox,
            self.airline4TotalShotsSpinBox,
            self.airline5TotalShotsSpinBox,
            self.airline6TotalShotsSpinBox,
            self.mSG_airline_TotalShotsSpinBox
        ]
        return list_of_airline_spinners

    def create_line_plot(self):
        """
        Creates a main line plot and events on it
        :return:
        """
        plot_list = db_service.return_records(self.connection)  # returns gunid, time, shots, id of the record

        basic_guns_data_for_plot_events = {}  # data structore for populating indivudual events on the line  # TODO Is this really necessery?

        for each in plot_list:
            gunid = each[0]
            id = each[3]
            time = datetime.datetime.strptime(each[1], "%d/%m/%Y %H:%M")
            shots = each[2]
            basic_guns_data_for_plot_events[id] = {'gunid': gunid, 'time': time, 'shots': shots}
            # print(basic_guns_data_for_plot_events)

        # for each in plot_list:
        #     print(f'One item: {each}')

        gun1_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 1]
        gun1_stats_shots = [i[2] for i in plot_list if i[0] == 1]

        gun2_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 2]
        gun2_stats_shots = [i[2] for i in plot_list if i[0] == 2]

        gun3_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 3]
        gun3_stats_shots = [i[2] for i in plot_list if i[0] == 3]

        gun4_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 4]
        gun4_stats_shots = [i[2] for i in plot_list if i[0] == 4]

        gun5_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 5]
        gun5_stats_shots = [i[2] for i in plot_list if i[0] == 5]

        gun6_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 6]
        gun6_stats_shots = [i[2] for i in plot_list if i[0] == 6]

        gun7_stats_time = [datetime.datetime.strptime(i[1], "%d/%m/%Y %H:%M") for i in plot_list if i[0] == 7]
        gun7_stats_shots = [i[2] for i in plot_list if i[0] == 7]

        self.MplWidget.canvas.axes.clear()
        # self.MplWidget.canvas.axes.xaxis.set_tick_params(rotation=45)
        self.MplWidget.canvas.figure.subplots_adjust(left=0.05, right=0.9, bottom=0.1, top=0.9)
        # self.MplWidget.canvas.figure.tight_layout()

        self.MplWidget.canvas.mpl_connect('pick_event', self.on_line_plot_event_click)

        gun_plot_1, = self.MplWidget.canvas.axes.plot(gun1_stats_time, gun1_stats_shots, label='Gun 1')
        gun_plot_2, = self.MplWidget.canvas.axes.plot(gun2_stats_time, gun2_stats_shots, label='Gun 2')
        gun_plot_3, = self.MplWidget.canvas.axes.plot(gun3_stats_time, gun3_stats_shots, label='Gun 3')
        gun_plot_4, = self.MplWidget.canvas.axes.plot(gun4_stats_time, gun4_stats_shots, label='Gun 4')
        gun_plot_5, = self.MplWidget.canvas.axes.plot(gun5_stats_time, gun5_stats_shots, label='Gun 5')
        gun_plot_6, = self.MplWidget.canvas.axes.plot(gun6_stats_time, gun6_stats_shots, label='Gun 6')
        gun_plot_msg, = self.MplWidget.canvas.axes.plot(gun7_stats_time, gun7_stats_shots, label='MSG')  # MSG GUN

        for record_id, gun_info in basic_guns_data_for_plot_events.items():  # TODO adds events to each gun plot indivudually

            if gun_info['shots'] == 0:  # means gun change (color red)

                temp_text = self.MplWidget.canvas.axes.text(gun_info['time'], gun_info['shots'], " ",
                                                            size=6,
                                                            ha="center", va="center",
                                                            bbox=dict(boxstyle="Circle",
                                                                      ec=(1., 0.5, 0.5),
                                                                      fc=(1., 0.8, 0.8),
                                                                      ), picker=5
                                                            )

                main_record_event = gun_events.GunEvent(temp_text, record_id, gun_info['gunid'])

                self.main_record_event_list.append(
                    main_record_event)  # stores a dict with keys as record_id and values as text objects for main events

        legend = self.MplWidget.canvas.axes.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0.,
                                                   loc='upper left')  # stores all the lines from the legend
        lines = [gun_plot_1, gun_plot_2, gun_plot_3, gun_plot_4, gun_plot_5, gun_plot_6, gun_plot_msg]

        for legline, origline in zip(legend.get_lines(), lines):
            legline.set_picker(5)  # 5 pts tolerance
            self.all_plots_dict[legline] = origline

        self.MplWidget.canvas.axes.set_title(
            'the fart of the mystery caves are well known throughout history for their unstopable booty smell')

        self.MplWidget.canvas.draw()

    ######################## SIGNALS AND EVENTS #########################################

    def on_line_plot_event_click(self, event):  # A method that runs when the user clicks on the red circle or legend
        this_point = event.artist

        # on the pick event, find the orig line corresponding to the
        # legend proxy line, and toggle the visibility
        if isinstance(event.artist, Line2D):  # this is used to create a toggle effect on the main line chart
            legline = event.artist
            origline = self.all_plots_dict[legline]
            vis = not origline.get_visible()
            origline.set_visible(vis)
            gun_number = origline.get_label()
            if gun_number is 'MSG':  # necessary as the plot is called "MSG" rather than gun 7 like everywhere else
                gun_number = int(7)
            else:
                gun_number = int(origline.get_label().split()[1])  # extracts number from the string e.g. 'Gun 1' = 1

            for each_event in self.main_record_event_list:
                if each_event.gun_id == gun_number:
                    each_event.text.set_visible(vis)
                    print('Set to ', vis)
            # self.red_circle_events_list[event.artist.get_gid()].set_visible(vis)
            # Change the alpha on the line in the legend so we can see what lines
            # have been toggled
            if vis:
                legline.set_alpha(1.0)
            else:
                legline.set_alpha(0.2)
            self.MplWidget.canvas.draw()
        elif isinstance(event.artist, Text):  # execute if red circle event is used
            self.update_text_fields(this_point)

    def button_clicked_copy_shots(self):
        """
        Copy all shots entered for guns to other spinners
        :return:
        """
        for each_gun_spinner, each_airline_spinner, each_tb_spinner, each_sol_spinner in zip(
                self.list_of_gun_spinners(),
                self.list_of_airline_spinners(),
                self.list_of_tb_spinners(),
                self.list_of_sol_spinners()):
            each_airline_spinner.setValue(each_gun_spinner.value())
            each_tb_spinner.setValue(each_gun_spinner.value())
            each_sol_spinner.setValue(each_gun_spinner.value())

    def button_clicked_add_new_record(self):  # Adds new record to the database via db_service function

        gun_number = 1
        gun_stats = []
        for gun_spinner, airline_spinner, airline_type, tb_spinner, sol_spinner in zip(self.list_of_gun_spinners(),
                                                                                       self.list_of_airline_spinners(),
                                                                                       self.list_of_airline_type_comboxes(),
                                                                                       self.list_of_tb_spinners(),
                                                                                       self.list_of_sol_spinners()):
            gun_stats.append({'gunid': gun_number,
                              'project': self.projectNameLineEdit.text(),
                              'gun_total_shots': gun_spinner.value(),
                              'previous_record': None,
                              'airline_type': airline_type.currentText(),
                              'date_time': self.dateAndTimeDateTimeEdit.dateTime().toString("dd/MM/yyyy hh:mm"),
                              'airline_shots': airline_spinner.value(),
                              'tb_total_shots': tb_spinner.value(),
                              'sol_total_shots': sol_spinner.value(),
                              'comment': self.comments_txt.toPlainText()
                              })
            gun_number += 1

        print('Clicked button', gun_stats)

        db_service.add_new_stats_for_gun(self.connection,
                                         gun_stats)  # adds new record to the database via db.service

    ######################## SIGNALS AND EVENTS #########################################

    def update_all_charts(self):  # TODO Finish update function as it currently doesn't owrk
        self.MplWidget.canvas.draw()
        self.MplLineWidget.canvas.draw()

    def update_text_fields(self, selected_record: Text):  # updates all text fields

        result = db_service.return_record(self.connection, selected_record.get_gid())

        print(result)
        self.recordIDLineEdit.setText(str(result[0][0]))
        self.gunNumberLineEdit.setText(str(result[0][1]))
        self.dateLineEdit.setText(str(result[0][2]))
        self.totalShotsLineEdit.setText(str(result[0][3]))
        self.totalAirlineShotsLineEdit.setText(str(result[0][4]))
        self.airlineTypeLineEdit.setText(str(result[0][5]))
        self.totalTBsShotsLineEdit.setText(str(result[0][6]))
        self.totalSolenoidShotsLineEdit.setText(str(result[0][7]))
        self.projectLineEdit.setText(str(result[0][8]))
        self.textBrowser.setText(str(result[0][9]))

    def create_bar_total_shots(self):
        """
        Creates the bar chart with the current total shots for each gun
        :param connection: connection to sqlite3 database
        :return: None
        """

        group = ['Gun 1', 'Gun 2', 'Gun 3', 'Gun 4', 'Gun 5', 'Gun 6', 'MSG']
        shots = []
        index = 1
        for each in group:
            shots.append(db_service.return_latest_total_shots_for_gun(self.connection, index))
            index += 1

        self.MplLineWidget.canvas.axes_guns_shots_bar_plot.clear()

        self.MplLineWidget.canvas.axes_guns_shots_bar_plot.barh(group, shots)

        self.MplLineWidget.canvas.axes_guns_shots_bar_plot.xaxis.grid(True, linestyle='--', which='major',
                                                                      color='grey', alpha=.25)
        # self.MplLineWidget.canvas.axes.axvline(200, ls='--', color='r')

        self.MplLineWidget.canvas.axes_guns_shots_bar_plot.set_title('Gun shots statistics')
        self.MplLineWidget.canvas.draw()

    def create_bar_airline_shots(self):
        """
        Creates bar char for the amount of shots done by each airline
        :param connection:
        :return:
        """
        group = ['Gun 1', 'Gun 2', 'Gun 3', 'Gun 4', 'Gun 5', 'Gun 6', 'MSG']
        shots = []
        index = 1
        for each in group:
            shots.append(db_service.return_latest_total_shots_for_airlines(self.connection, index))
            index += 1

        self.MplLineWidget.canvas.axes_airline_shots_plot.clear()
        self.MplLineWidget.canvas.axes_airline_shots_plot.barh(group, shots, color='purple')

        self.MplLineWidget.canvas.axes_airline_shots_plot.xaxis.grid(True, linestyle='--', which='major',
                                                                     color='grey', alpha=.25)

        self.MplLineWidget.canvas.axes_airline_shots_plot.set_title('Airline shots statistics')
        self.MplLineWidget.canvas.draw()

    def create_bar_tbs_shots(self):
        """
        Creates bar char for the amount of shots done by each Time Break
        :param connection:
        :return:
        """
        group = ['Gun 1', 'Gun 2', 'Gun 3', 'Gun 4', 'Gun 5', 'Gun 6', 'MSG']
        shots = []
        index = 1
        for each in group:
            shots.append(db_service.return_latest_total_shots_for_tbs(self.connection, index))
            index += 1

        self.MplLineWidget.canvas.axes_tbs_plot.clear()
        self.MplLineWidget.canvas.axes_tbs_plot.barh(group, shots, color='black')
        self.MplLineWidget.canvas.axes_tbs_plot.xaxis.grid(True, linestyle='--', which='major',
                                                           color='grey', alpha=.25)
        self.MplLineWidget.canvas.axes_tbs_plot.set_title('Timebreak shots statistics')
        self.MplLineWidget.canvas.draw()

    def create_bar_solenoids_shots(self):
        """
        Creates bar char for the amount of shots done by each Time Break
        :param connection:
        :return:
        """
        group = ['Gun 1', 'Gun 2', 'Gun 3', 'Gun 4', 'Gun 5', 'Gun 6', 'MSG']
        shots = []
        index = 1
        for each in group:
            shots.append(db_service.return_latest_total_shots_for_solenoids(self.connection, index))
            index += 1

        self.MplLineWidget.canvas.axes_solenoids_bar_plot.clear()
        self.MplLineWidget.canvas.axes_solenoids_bar_plot.barh(group, shots, color='aqua')
        self.MplLineWidget.canvas.axes_solenoids_bar_plot.xaxis.grid(True, linestyle='--', which='major',
                                                                     color='grey', alpha=.25)
        self.MplLineWidget.canvas.axes_solenoids_bar_plot.set_title('Solenoids shots statistics')
        self.MplLineWidget.canvas.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Natalia is the BEST")
    app.setStyle('Fusion')
    # qtmodern.styles.light(app)

    window.show()

    app.exec()


def add_record():
    """
    Adds new record to the log
    :return:
    """
    pass


def display_main_chart():
    """
    Displays matplotlip charts
    :return:
    """


if __name__ == '__main__':
    main()
