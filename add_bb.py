import praw
import random
import time

def main():
	reddit = praw.Reddit(client_id="zbBOz1kpD9YEzg",
                     client_secret="dMaDsOsXi8OKMcWNP0HjsxfAjZb9OQ",
                     password="wef98wbeforthyte",
                     user_agent="Python Script",
                     username="Au_Vantablack")
	targetSub = "BubbleBreaker"
	subreddits = input("Enter Subreddits: ")
	comments_g = reddit.subreddit(subreddits).comments(limit=None)
	tot_comments = 0
	comments = []
	
	for item in comments_g:
		comments.append(item)
		tot_comments+=1
	print("Total comments fetched = "+str(tot_comments))
	no = [] 
	for contributor in reddit.subreddit(targetSub).contributor(limit=None): 
		no.append(contributor.name) 
	to_add = int(input("Enter Number: "))
	i = 0 
	j = 0
    
	for comment in comments:
		try:
			if comment.author.name not in no and j>=i*tot_comments/(to_add+1):
				i+=1 
				if i>to_add:
					break
				print(str(i)+": "+comment.permalink+" created "+str(int(((time.time()-comment.created_utc)/3.6))/1000)+" hours ago.")
				reddit.subreddit(targetSub).contributor.add((comment.author).name)	
		except:
			print("Error: "+comment.permalink)		
		j+=1			

if __name__ == '__main__':
	main()