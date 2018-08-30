import matplotlib.pyplot as plt
from matplotlib import style
from act_time import get_minute


def create_plot(name_files, out_plot_name):
    style.use("fivethirtyeight")
    plt.title("Ceny iPhone 8")
    plt.xlabel("czas")
    plt.ylabel("cena [zł]")
    for file in name_files:
        data = open('data/' + file + '.txt', 'r')
        graph_data = data.read()
        lines = graph_data.split("\n")
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(float(y))
        plt.plot(xs, ys, label=file)
        plt.xticks(xs, rotation='vertical')
        plt.legend(loc=2)
        data.close()
    plt.savefig('server/'+out_plot_name, bbox_inches='tight', dpi=1000)


def create_plot_thread(name_files, out_plot_name, write_minutes, operation_minutes):
    DONE = False
    CAN_BE_DONE = True

    state = CAN_BE_DONE

    while True:

        if get_minute() == write_minutes and state == CAN_BE_DONE:
            create_plot(name_files, out_plot_name)
            state = DONE
        elif get_minute() == (write_minutes + operation_minutes) % 60 and state == DONE:
            state = CAN_BE_DONE
        else:
            print("Waiting for plot")