# Data
digits <- c(1, 2, 3, 4, 5, 6)
frequency <- c(7, 2, 6, 3, 4, 8)

# Create labels with digits
labels <- paste("Dice ", digits, sep = "")

# Plot pie chart
pie(frequency,
    labels = labels,
    main = "Pie Chart of Dice Roll Frequencies",
    col = rainbow(length(frequency)),
    clockwise = TRUE)
