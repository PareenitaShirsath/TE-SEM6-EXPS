
# Scatter Plot of `mpg` Dataset using `ggplot2`

```r
# Load ggplot2
library(ggplot2)

# Scatter plot of mpg dataset
ggplot(mpg, aes(x = displ, y = hwy, color = class)) +
  geom_point() +
  labs(title = "Engine Displacement vs Highway MPG", 
       x = "Displacement (L)", 
       y = "Highway MPG") +
  theme_minimal()
