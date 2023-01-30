import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write("# The Garen-inator")

max_health = st.number_input('Max Health', step=100)
tech = (st.slider('Quickblades Crit Chance', min_value=0, max_value=100, step=5) * 0.002) + 1

collect = st.checkbox('COLLECTOR?')
if collect:
    sex = 0.05 * max_health
else:
    sex = 0

# st.write('### Damage by Level')
category_names = ['Kill Zone', 'Missing Health']
results = {
    'Level Six': [int((120 + 0.20 * max_health) * tech + sex), int((max_health -(120 + 0.20 * max_health) * tech - sex))],
    'Level Eleven': [int((230 + 0.2308 * max_health) * tech + sex), int((max_health -(230 + 0.2308 * max_health) * tech - sex))],
    'Level Sixteen': [int((333 + 0.2593 * max_health) * tech + sex), int((max_health -(333 + 0.2593 * max_health) * tech - sex))],
}

def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.7,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white'
        ax.bar_label(rects, label_type='center', color=text_color, fontsize='xx-large')
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='medium')

    return fig, ax


survey(results, category_names)
st.pyplot(plt)