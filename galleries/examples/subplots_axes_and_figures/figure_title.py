"""
=============================================
Figure labels: suptitle, supxlabel, supylabel
=============================================

Each axes can have a title (or actually three - one each with *loc* "left",
"center", and "right"), but is sometimes desirable to give a whole figure
(or `.SubFigure`) an overall title, using `.FigureBase.suptitle`.

We can also add figure-level x- and y-labels using `.FigureBase.supxlabel` and
`.FigureBase.supylabel`.
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import get_sample_data

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

# %%
# A global x- or y-label can be set using the `.FigureBase.supxlabel` and
# `.FigureBase.supylabel` methods.


def convertdate(x):
    return np.datetime64(x, 'D')

fname = get_sample_data('Stocks.csv', asfileobj=False)
stocks = np.genfromtxt(fname, encoding='utf-8', delimiter=',',
                       names=True, dtype=None, converters={0: convertdate},
                       skip_header=1)

fig, axs = plt.subplots(4, 2, figsize=(9, 5), layout='constrained',
                        sharex=True, sharey=True)
for nn, ax in enumerate(axs.flat):
    column_name = stocks.dtype.names[1+nn]
    y = stocks[column_name]
    line, = ax.plot(stocks['Date'], y / np.nanmax(y), lw=2.5)
    ax.set_title(column_name, fontsize='small', loc='left')
fig.supxlabel('Year')
fig.supylabel('Stock price relative to max')
