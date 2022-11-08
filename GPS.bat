set GMT_SESSION_NAME=29
gmt begin figure4 png
    gmt coast -JH15c -Rg -Baf -W0.5p 
    #gmt plot  -St0.05c gps456.txt -Gred
    #绘制大小不一的图
    gmt plot  -Sc -Gred -W1p M2_10.txt 

gmt end show
