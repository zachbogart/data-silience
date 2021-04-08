# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # "JupyTuesday: TidyTuesday Example in Python"
# > "Quick and dirty try of TidyTuesday data in a Jupyter Notebook"
#
# - toc: false
# - branch: master
# - badges: false
# - comments: true
# - categories: [python, jupytuesday, seaborn, altair]
# - image: "images/thumbnails/39623169081_f7f1f722ab_c.jpeg"
# - hide: false
# - search_exclude: false

# ![](my_icons/noun_Honeycomb_3644796.png)

# > Important: This post is hard to read. Experimenting with generating a notebook and posting it without a lot of extra work. Might try recording creation of a post sometime. But for now, this post is hard to parse as a user experience, although it does have an Altair graph you can poke and prod at the end...

# - From [TidyTuesday](https://github.com/rfordatascience/tidytuesday), read in the data and get to a visualization with Seaborn and Altair 
# - Quite rough, thinking it might be beneficial to try recording making a notebook...

# +
#collapse
import pandas as pd

transit_cost = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-05/transit_cost.csv')
# -

transit_cost.isnull().sum()

# remove null values for ID
transit_cost = transit_cost[~transit_cost.e.isnull()]

# ## For the tracks that are completed, what is the relationship between cost and distance?

transit_cost.tunnel_per.value_counts().head()

# - most of the tunnels are completed

# need to remove two tunnels that don't have cost per km
completed = transit_cost[
    (transit_cost.tunnel_per == '100.00%') & 
    (~transit_cost.cost_km_millions.isnull())
]

# no nulls for cost_km_millions or length
completed.isnull().sum()

# grouping test
# mean and counts for cost_km_millions by country
completed.groupby('country')['cost_km_millions'].agg(['mean', 'count']).sort_values('mean', ascending=False).head(10)

# +
# aggregate columns
compare = completed.groupby('country').agg(
    {
        'cost_km_millions': ['mean', 'count'],
        'length': ['mean']
    }
)

# rename the multiIndex
compare.columns = ['__'.join(col).strip() for col in compare.columns.values]
compare.reset_index(inplace=True)
# -

compare.head()

# ## Seaborn

# +
#collapse
import seaborn as sns

sns.relplot(
    data=compare,
    x='cost_km_millions__mean',
    y='length__mean',
    size='cost_km_millions__count'
)
# -

# ## Altair

# + jupyter={"outputs_hidden": true}
#hide
# ! pip install altair vega_datasets

# +
#collapse
import altair as alt

alt.Chart(compare).mark_circle(size=50).encode(
    x=alt.X('cost_km_millions__mean', axis=alt.Axis(title='Average Cost per Kilometer ($Million/km)')),
    y=alt.Y('length__mean', axis=alt.Axis(title='Average Length (km)')),
    tooltip=['country', 'cost_km_millions__mean', 'length__mean'],
).properties(
    title='Dig Dug: Building Tunnels'
).configure_mark(
    opacity=0.7
).configure_title(
    fontSize=24
    
).interactive()
# -

# #### Image Credit
# - [Honeycomb](https://thenounproject.com/term/honeycomb/3644796/) by Zach Bogart from the [Noun Project](https://thenounproject.com/zachbogart/)
# - [Three women cricket spectators picnicking](https://flic.kr/p/23nn6HB) from "State Library of New South Wales" on Flickr Commons


