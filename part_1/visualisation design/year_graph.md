# Meteorite Landings by Year

## Questions Addressed
1. What **patterns** have emerged in meteorite landings over the years?
2. How many landings have been observed **compared to** meteorites that were discovered after landing over the years?
3. How (if at all) is the year of meteorite landing **related to** 
   1. the geographical distribution of meteorite landings
   2. year of meteorite landing/ discovery
   3. meteorite mass

## Visualisation: Line Graph
A line graph was chosen to address the questions related to yearly data as this medium is well suited to showing trends in how
data has changed over time. To address question two, the data is divided into separate lines to show the meteorite landings that
were observed falling, those that were found later, and the total value of all the landings. The data filters in the control box
enable the user to manipulate various factors to address question 3.

**line graph with hover functionality**:
![](/part_1/visualisation%20design/images/line%20graph.png)

**colour palette:**
![](/part_1/visualisation%20design/images/discovery%20colour%20palette.png)

## Explanation

The mode of meteorite discovery is categorical data so another divergent colour palette is used to differentiate between the different
values. It uses cold colours in contrast to the warmer tones of the colour palette associated with meteorite category in order to avoid
confusion between the two forms of colour categorisation. This is important as the map, which may have markers coordinated to category
enabled, is visible alongside the line graph. The lines corresponding to meteorites seen falling ("fell") and found later
("found") are in coloured distinguishable shades of green, while the line corresponding to the total of all the landings in a given year
("all) is further distinguished in purple.

A hover functionality was included to add a more dynamic feel to the graph as well as to provide an explicit link between the visualisation
and the numbers, an important consideration for the educational goals of the target audience. The hover functionality is unified along the
x-axis, so the user can see the values for all the visible categories in one box at once, with a dashed line that follows the mouse horizontally
along the x-axis. This is useful in giving the user a natural progression along the timescale and enabling convenient comparisons between different
modes of discovery. Additionally, the vertical alignment of the hover feature improves coherence and reduces clutter considering that the data does not
progress smoothly.

Also in the interest of reducing clutter, the default setting is that only the lines corresponding "fell" and "found" are visible when the graph is first presented;
the line corresponding to "all" is hidden unless the user manually selects it on the legend. This is a justifiable design choice considering that the "fell" and "found"
data are included in the "all" category anyway, and the closeness of "found"  and "all" values means that when both lines are visible at once, one tends
to obscure the other.

## Evaluation

The initial design refrained from plotting data points for years when no landings were recorded. This resulted in the y-axis beginning at 1, and
meant that certain selected time-intervals would reveal no points on the graph (if there was never more than one landing per year in a given time
period) despite landings having been recorded. This was adjusted after noting Unwin's remark that not ncluding zero in a scale ought to
"make the reader wonder if some deception is being practiced" (Unwin et al., 2008). Although the target audience is unlikely to be "suspicious"
given their level of experience, this kind of unconventional scaling would certainly be a potential point of confusion which misleads and
undermines the educational gial. The years with no corresponding data were therefore replaced with zero values and the y-axis adjusted to
start at zero, which resulted in a much cleaner look first the graph overall.