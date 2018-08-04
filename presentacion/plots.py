import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


plots = {
    'capital-common-countries': [0.8125, 0.805147, 0.779412, 0.878676, 0.860294, 0.882353, 0.928105, 0.871345],
    'capital-world': [0.625969, 0.642442, 0.631783, 0.790698, 0.796512, 0.804264, 0.882988, 0.883377],
    'currency': [0.0576923, 0.0576923, 0.0384615, 0.0384615, 0.0384615, 0.0192308, 0.153846, 0.153846],
    'city-in-state': [0.106212, 0.0961924, 0.0881764, 0.236473, 0.218437, 0.246493, 0.301711, 0.386691],
}
plots2 = {
    'family': [0.794118, 0.797386, 0.800654, 0.928105, 0.921569, 0.921569, 0.797794, 0.885621 ],
    'gram1-adjective-to-adverb': [0.283333, 0.266667, 0.27381, 0.342857, 0.340476, 0.338095, 0.283626, 0.37619],
    'gram2-opposite': [0.340909, 0.333333, 0.333333, 0.378788, 0.378788, 0.386364, 0.309091, 0.333333],
    'gram5-present-participle': [0.71, 0.708333, 0.706667, 0.77, 0.766667, 0.766667, 0.784585, 0.800395],
}
plots3 = {
    'gram6-nationality-adjective': [0.834401, 0.822507, 0.838975, 0.926807, 0.923147, 0.924977, 0.924138, 0.930782],
    'gram7-past-tense': [0.258333, 0.263333, 0.261667, 0.315, 0.308333, 0.31, 0.227273, 0.23913],
    'gram8-plural': [0.594758, 0.592742, 0.573589, 0.694556, 0.702621, 0.699597, 0.523656, 0.772043],
    'gram9-plural-verbs': [0.416667, 0.403333, 0.401667, 0.505, 0.506667, 0.518333, 0.458462, 0.493333],
}
total = {
    'total': [0.555168, 0.55244, 0.548954, 0.65247, 0.651864, 0.656411, 0.635094, 0.677529]
}



def plot_data(data_dir, plot_title, objects, y_min=0, y_max=1, n=None):
    plt.figure(1, (15,8))
    for title, values in data_dir.items():
        if n is not None:
            plt.subplot(n)
            if n == 211:
                n = 222
            n += 1
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, values, align='center', width=0.5, color=['black', 'red', 'green', 'blue', 'cyan', 'pink', 'purple', 'orange'], alpha=0.9)
        plt.xticks(y_pos, objects)
        plt.ylim(y_min, y_max)
        plt.ylabel('Accuracy')
        plt.title(title)
    plt.savefig(plot_title + '.png')
    plt.close()

objects = ("100_1", "100_2", "100_3", "300_1", "300_2", "300_3", "Cristian", "FastText")
n = 221
title = 'plot1'
plot_data(plots, title, objects=objects, n=n)
title = 'plot2'
plot_data(plots2, title, objects=objects, n=n)
title = 'plot3'
plot_data(plots3, title, objects=objects, n=n)
title = 'total'
plot_data(total, title, objects=objects)
#


#objects = ("100_1", "100_1_new", "100_2", "100_2_new", "100_3", "100_3_new", "Cristian")
#
#n = 211
#title = "tagger1"
#known_acc = {
#"Unknown accuracy": [x / 100 for x in [89.17, 90.15, 89.46, 89.98, 89.31, 90.03, 88.22]],
#"Total accuracy": [x / 100 for x in [96.57, 96.68, 96.61, 96.65, 96.58, 96.65, 96.47]],
#"Known accuracy": [x / 100 for x in [97.38, 97.40, 97.39, 97.39, 97.38, 97.38, 97.38]],
#
#}
#plot_data(known_acc, title, objects, n=n)
#
#title = "tagger2"
#total_acc = {
#"Total accuracy": [x / 100 for x in [96.57, 96.68, 96.61, 96.65, 96.58, 96.65, 96.47]]
#}
#plot_data(total_acc, title, objects)
#
#title = "tagger3"
#unk_acc = {
#"Unknown accuracy": [x / 100 for x in [89.17, 90.15, 89.46, 89.98, 89.31, 90.03, 88.22]]
#}
#plot_data(unk_acc, title, objects)
