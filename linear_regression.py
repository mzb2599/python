def linear_regression(x,y,z):
    #Mean calculation
    xbar=sum(x)/len(x)
    #xbar=round(xbar,4)
    #print(xbar)
    ybar=sum(y)/len(y)
    #print(ybar)


    #B0 and B1 calculation
    xi_xbar =list()
    yi_ybar =list()
    xi_xbar_square=list()
    xi_xbar_yi_ybar=list()
    RSS_y = list()
    yi_y = list()
    yi_y_square = list()

    for i in range(len(x)):
        xi_xbar.append(x[i]-xbar)
        yi_ybar.append(y[i] - ybar)
        
    for i in range(len(x)):
        xi_xbar_square.append(xi_xbar[i] * xi_xbar[i])
        xi_xbar_yi_ybar.append(xi_xbar[i] * yi_ybar[i])
        
    B1 = sum(xi_xbar_yi_ybar) / sum(xi_xbar_square)
    B0 = ybar - B1 * xbar
    
    for i in range(len(x)):
        RSS_y.append(B0 + B1 * x[i])
        yi_y.append(y[i] - RSS_y[i])
        yi_y_square.append(yi_y[i] * yi_y[i])
        RSS=sum(yi_ybar)
    
    y_final = B0 + B1 * z
    return y_final

result=linear_regression([1,2,4],[2,3,6],3)
print(result)