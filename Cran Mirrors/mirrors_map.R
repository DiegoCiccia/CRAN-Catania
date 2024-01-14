library(ggplot2)
library(grid)
library(sf)
library(dplyr)
library(rnaturalearth)

df <- read.csv("Cran Mirrors/mirrors.csv", encoding = "utf8")
df$nation[df$nation == "USA"] <- "United States"
df$nation[df$nation == "UK"] <- "United Kingdom"
df <- subset(df, !(df$nation %in% c("0-Cloud", "Worldwide")))
df_coord <- read.csv("Cran Mirrors/mirrors_coord.csv", encoding = "utf8")

world_map <- ne_countries(scale = 50, returnclass = 'sf')
cran_map <- world_map %>% filter(.data$name %in% levels(factor(df$nation)))

ggplot() + 
  geom_sf(data = world_map, fill = 'white') + 
  geom_sf(data = cran_map, fill = 'gray') +
  geom_point(data = df_coord, aes(x = x, y = y), colour = "red", cex = 2, fill = "red") +
  theme_void() + ggtitle("CRAN mirrors around the world") +
  theme(plot.title = element_text(hjust = 0.5))
ggsave("cran_world.pdf")

euplus <- c("Austria","Belgium","Bulgaria","Croatia","Cyprus",
                   "Czech Rep.","Denmark","Estonia","Finland","France",
                   "Germany","Greece","Hungary","Ireland","Italy","Latvia",
                   "Lithuania","Luxembourg","Malta","Netherlands","Poland",
                   "Portugal","Romania","Slovakia","Slovenia","Spain",
                   "Sweden")

world_map <- world_map %>% filter(.data$name %in% levels(factor(euplus)))
df_coord <- df_coord %>% filter(.data$nation %in% levels(factor(euplus)))
cran_map <- world_map %>% filter(.data$name %in% levels(factor(df$nation)))
ggplot() + 
  geom_sf(data = world_map, fill = 'white') + 
  geom_sf(data = cran_map, fill = 'gray') +
  geom_point(data = df_coord, aes(x = x, y = y), colour = "red", cex = 2, fill = "red") +
  theme_void() + ggtitle("CRAN mirrors around EU") +
  theme(plot.title = element_text(hjust = 0.5))
ggsave("cran_euplus.pdf")