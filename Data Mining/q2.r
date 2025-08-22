# Data
year <- c("2001", "2002", "2003")
export <- c(26, 32, 35)
import <- c(35, 40, 50)
# Combine Export and Import into a matrix
data <- rbind(export, import)
# Create bar plot
barplot(data,
        beside = TRUE,                     # Side-by-side bars
        names.arg = year,                  # Year labels
        col = c("skyblue", "orange"),      # Colors for export/import
        main = "Export and Import (2001–2003)",
        xlab = "Year",
        ylab = "Value")
# Add legend
legend("topright",
       legend = c("Export", "Import"),
       fill = c("skyblue", "orange"))
