This is a simple program to automate ordering groceries online from [BigBasket](http://www.bigbasket.com). I have used `selenium` with `python` bindings after having experimented with `requests`, `urllib2`, `twill` and `mechanize`. The program is very primitive as of yet and I have listed some `TODO's` which I will handle in the coming time as and when I need. 

###Usage : 
#####Add items to your shopping list : 
    
    python add.py <item1> <item2> ... <itemN>

#####Running the program : 
There are two ways:

1. You can either run the program yourself as and when you need.
		
    ```python BigBasket.py```

2. You can list it as a `cronjob`. There is cron file in there which by default will run the program every 8 hours. Feel free to [modify it](https://help.ubuntu.com/community/CronHowto) to suit your needs.
Here is how you list the file as a crontab.
		
    ```crontab bb_cron```

Either ways, the program will fire up Firefox and add all the items listed in your shopping list to your cart. After it goes to the final checkout page it posts a notification (This is exclusively for osx) prompting you to take an action.

###Limitations : 

1. It picks out the first element from the list of search results. It might not always be what you want it to be. I will change that. Eventually.
2. You can not add the quantity of items to order, yet.
3. You have to manually remove items from the shopping list.

Let me know if there are others.
