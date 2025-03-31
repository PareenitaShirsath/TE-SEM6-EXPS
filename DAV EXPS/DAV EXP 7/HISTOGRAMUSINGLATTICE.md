# Histogram of `Sepal.Length` in `iris` Dataset using `lattice`

```r
# Load lattice
library(lattice)

# Histogram of Sepal.Length in iris dataset
histogram(~Sepal.Length, data = iris, 
          main = "Histogram of Sepal Length", 
          xlab = "Sepal Length", 
          col = "blue")
