sns.barplot(x=df['Category'], y=df['Sales'])
when i execute this i found that there is some black lines 
those are errorbars , seaborn use it to calculate the confidence interval
[ 1. Pick N values randomly (with replacement) ]
                              │
                              ▼
                     [ 2. Calculate Mean ]
                              │
                              ▼
                     [ 3. Repeat 1,000 times ]
                              │
                              ▼
                     [ 4. Sort all 1,000 means ]
                              │
                              ▼
         ┌────────────────────┴────────────────────┐
         │                                         │
 2.5th Percentile                          97.5th Percentile
 (Bottom of line)                           (Top of line)

------------------------------------------------------------------------------------


