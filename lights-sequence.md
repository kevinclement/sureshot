## ➿➿ Wiring Ordering Under Playfield ➿➿


===========================================================

| 💡  | 🔌 |
| :--- | ---: |
| l_5_top | 1-0 |
| l_popbumper_right | 1-1|


```mermaid
    flowchart LR
        A["l_5_top (1-0)"] ==> B["l_popbumper_right"] ==> C["l_3_top"] ==> D["l_1"] ==> E["l_special_top"] ==> F["l_2_top"] ==> G["l_4_top"]
    flowchart LR
        H["l_special_left"] ==> I["l_popbumper_left"] ==> J["l_10"] ==> K["l_6"] ==> L["l_13"] ==> M["l_4"] ==> N["l_2"] 
    flowchart LR
        O["l_7"] ==> P["l_trough_1"] ==> Q["l_trough_2"] ==> R["l_trough_3"] ==> S["l_trough_4"] ==> T["l_trough_5"] 
    flowchart LR        
        U["l_trough_6"] ==> V["l_triangle_15"] ==> W["l_triangle_13"]
```

l_5_top             1-0
l_popbumper_right   1-1   
l_3_top			    1-2
l_1			        1-3
l_special_top		1-4
l_2_top			    1-5
l_4_top			    1-6
l_special_left      1-7
l_popbumper_left	1-8
l_10			    1-9
l_6			        1-10
l_13			    1-11
l_4			        1-12
l_2			        1-13
l_7			        1-14
l_trough_1			1-15
l_trough_2			1-16
l_trough_3			1-17
l_trough_4			1-18
l_trough_5			1-19
l_trough_6          1-20
l_triangle_15		1-21
l_triangle_13		1-22
l_triangle_10		1-23
l_triangle_6		1-24
l_triangle_4		1-25
l_popbumper_middle	1-26
l_12			    1-27
l_15			    1-28
l_triangle_2		1-29
l_triangle_1		1-30
l_triangle_3		1-31
l_triangle_5		1-32
l_triangle_9		1-33
l_triangle_8		1-34
l_triangle_7		1-35
l_triangle_12		1-36
l_triangle_14		1-37
l_triangle_11		1-38
l_8		        	1-39
l_3			        1-40
l_5			        1-41
l_14			    1-42
l_9			        1-43
l_11			    1-44
l_special_right     1-45

===========================================================

<details><summary>RAW ordering</summary>
<p>

```
(1-0) l_5_top > l_popbumper_right > l_3_top > l_1 > l_special_top > l_2_top > l_4_top > l_special_left > l_popbumper_left > l_10 > l_6 > l_13 > l_4 > l_2 > l_7 > 
l_trough_1 > l_trough_2 > l_trough_3 > l_trough_4 > l_trough_5 > l_trough_6 > l_triangle_15 > l_triangle_13 > l_triangle_10 > l_triangle_6 > l_triangle_4 > l_popbumper_middle > l_12 > l_15 > l_triangle_2 > l_triangle_1 > l_triangle_3 > l_triangle_5 >  l_triangle_9 > l_triangle_8 > l_triangle_7 > l_triangle_12 > l_triangle_14 > l_triangle_11 > l_8 > l_3 > l_5 > l_14 > l_9 >  l_11 > l_special_right
```

</p>
</details>