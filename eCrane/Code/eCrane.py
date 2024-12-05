import os, collections, json, tkinter, random
import matplotlib.pyplot as plt
import matplotlib as mlt
base_path = os.path.dirname(__file__)
config_path = os.path.join(base_path, "config.json")
config_dict = json.loads(open(config_path, encoding="utf-8").read())
def collect_file_statistics(path_to_analyze):
    filenames_list = os.listdir(path_to_analyze)
    list_of_files_types = list()
    for file_name in filenames_list:
        list_of_files_types.append(file_name.split('.')[-1])
    counted_file_types_dict = collections.Counter(list_of_files_types)
    return counted_file_types_dict

def draw_the_plot(counted_file_types_dict):
    labels = list(counted_file_types_dict.keys())
    numbs = list(counted_file_types_dict.values())
    plt.xticks(rotation=90)
    plt.title(config_dict["title"])
    plt.bar(labels,numbs, color="lime")
    plt.show()

def draw_main_menu():
    colors = list(mlt.colors._colors_full_map.values())
    next_color = 1
    menu = tkinter.Tk()
    menu.title("eCrane")
    menu.geometry("1080x675")
    menu = refrech_the_button(menu)
    global change_color_button
    change_color_button = tkinter.Button(text="Change color", bg=colors[next_color], command=next_color)
    change_color_button.pack()
    menu.mainloop()


def refrech_the_button(menu):
    change_color_button.pack_forget()
    change_color_button.pack()


if __name__ == "__main__":
    counted_file_types_dict = collect_file_statistics(config_dict["path_to_analyze"])
    #draw_the_plot(counted_file_types_dict)
    draw_main_menu()
