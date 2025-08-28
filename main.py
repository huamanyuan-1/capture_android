import argparse
from beans.youtube import Youtube
from beans.reddit import Reddit
if __name__ == "__main__":
    # test()
    # global mode
    parser = argparse.ArgumentParser(description='manual to this script')
    # app name
    parser.add_argument('-a', '--app', type=str, default = 'youtube', dest = 'app', help ='add your app name, if you want to test, input test')
    # function name
    # parser.add_argument('-f', '--func', type=str, default = 'search', dest = "func", help='add your function name, open or map') 
    # count
    # parser.add_argument('-c', '--count', type=int, default = 1000, dest = 'count', help = 'add your count, how many times you want to run the app')
    
    args = parser.parse_args()
    
    app = args.app
    # count = args.count
    # app_func = args.func
    
    if app == "youtube":
        youtube = Youtube(app=app)
    elif app == "reddit":
        reddit = Reddit(app=app)



        
       