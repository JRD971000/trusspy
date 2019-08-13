<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

         _____                  ______      
        |_   _|                 | ___ \     
          | |_ __ _   _ ___ ___ | |_/ /   _ 
          | | '__| | | / __/ __||  __/ | | |
          | | |  | |_| \__ \__ \| |  | |_| |
          \_/_|   \__,_|___/___/\_|   \__, |
                                       __/ |
                                      |___/ 
        
        TrussPy - Object Oriented Truss Solver for Python
                  Version 2019.08 (Build 201908)

        Author: Dutzler A.
                Graz University of Technology, 2018-2019
                
        TrussPy  Copyright (C) 2019  Andreas Dutzler
        This program comes with ABSOLUTELY NO WARRANTY; 
        for details type `trusspy.show_w()'.
        This is free software, and you are welcome to redistribute it
        under certain conditions; type `trusspy.show_c()' for details.
        

# Initialize Model
* loading Managers

    - finished.

[1 2 3] [2] [ True False  True]
[1 2 3] [2 1 3] [False False False]

# Model Summary
    Analysis Dimension      "ndim": 3
    Number of Nodes       "nnodes": 3
    Number of Elements    "nelems": 2
 
    System DOF              "ndof": 9
    active DOF             "ndof1": 1
    locked DOF             "ndof2": 8
 
    active DOF          "nproDOF1": [5]
    fixed  DOF          "nproDOF0": [0 1 2 3 4 6 7 8]
\pagebreak
 
# Run Simulation

## Summary of Analysis Parameters
|Description                          |Parameter|Value|
|:------------------------------------|:--------|:--|
|Maximum increments                   |   `incs`| 10 |
|Maximum increment recycles           |   `cycl`| 4 |
|Maximum Newton-Rhapson iterations    |   `nfev`| 8 |
|Maximum incremental displacement     |     `du`| 0.02 |
|Maximum incremental LPF              |   `dlpf`| 0.02 |
|Initial control component            |     `j0`| LPF|
|Locked control component             |`j_fixed`| False |
|Maximum incremental overshoot        |  `dxtol`| 1.000001 |
|Tolerance for x                      |   `xtol`| 8 |
|Tolerance for f                      |   `ftol`| 8 |

### Adaptive control for incremental stepwidth
|Description                          |Parameter    |Value|
|:------------------------------------|:------------|:--|
|Adaptive control for inc. stepwidth  |`stepcontrol`| True |
|Minimum step size factor             |     `minfac`| 1e-06 |
|Maximum step size factor             |     `maxfac`| 4 |
|Reduce step size factor              |     `reduce`| 0.125 |
|Increase step size factor            |   `increase`| 0.5 |


## Step 1
* i(1) is index with 1st-biggest component in abs(Dx/Dx,max).
* i(2) is index with 2nd-biggest component in abs(Dx/Dx,max).
* i(3) is index with 3rd-biggest component in abs(Dx/Dx,max).
* i(4) is index with 4th-biggest component in abs(Dx/Dx,max).
* Value(i) is value of i-th component in abs(Dx/Dx,max).
$$\text{Value}_i = \left|\frac{D_x}{D_{x,max}}\right|_i$$

### Increment 1
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   2   |4.303e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6964|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.01393

### Increment 2
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |4.079e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6705|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.03213

### Increment 3
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |7.852e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6340|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.05548

### Increment 4
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |1.532e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.5817|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.08456

### Increment 5
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |3.040e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.5055|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:     0.1189

### Increment 6
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |6.131e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.3928|   0|     nan|

* final LPF:      0.155

### Increment 7
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |5.048e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.2609|   0|     nan|

* final LPF:     0.1759

### Increment 8
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |5.338e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.1297|   0|     nan|

* final LPF:     0.1863

### Increment 9
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |5.483e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.0064|   0|     nan|

* final LPF:     0.1858

### Increment 10
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |5.419e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.1427|   0|     nan|

* final LPF:     0.1743
\pagebreak
 

### Create result object from analysis results for step   1

    write result   1/ 10 (LPF:    0.01393)
    write result   2/ 10 (LPF:    0.03213)
    write result   3/ 10 (LPF:    0.05548)
    write result   4/ 10 (LPF:    0.08456)
    write result   5/ 10 (LPF:     0.1189)
    write result   6/ 10 (LPF:      0.155)
    write result   7/ 10 (LPF:     0.1759)
    write result   8/ 10 (LPF:     0.1863)
    write result   9/ 10 (LPF:     0.1858)
    write result  10/ 10 (LPF:     0.1743)

End of Step 1
\pagebreak
 

## Job duration
Time measurement for execution times of "Model.build()" and "Model.run()".

    total  cpu time "build":      0.001 seconds
    total wall time "build":      0.000 seconds

    total  cpu time "run":        0.113 seconds
    total wall time "run":        0.125 seconds

