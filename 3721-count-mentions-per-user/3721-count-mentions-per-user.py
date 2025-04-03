'''task: Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.

input: numberOfUsers and array events

events[i] will either be:
["MESSAGE", "timestampi", "mentions_stringi"]
mention string can contain either a single id of who is mentioned or multiple ids seperated 
by a whitespace
ALL mentions all users including offline
HERE mentions all online users

["OFFLINE", "timestampi", "idi"]
id went offline and will automatically go back online after 60 time units

observations:
array mentions will always be numberOfUsers - 1 size
mentions = []

mention string may contain duplicates
parse events array extracting the message type, time, id
handle going online from offline before any message events if they are in the same timestamp
check for ALL or HERE events in the mention string
ALL increments all ids by 1 mention
HERE increments only online ids by 1 mention
'''
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # initializes a list of zeros, one for each user, to track mentions.
        mentions = [0] * numberOfUsers 
        # list indicating online status for each user, initially setting all to 1 
        is_online = [1] * numberOfUsers
        # sorts events by time and then event type, prio to offline
        events.sort(key = lambda x: (int(x[1]), x[0] != "OFFLINE"))
        print(events)

        for message, time, ids in events:
            # if they are offline set their time to 60 more than current time
            if message == "OFFLINE":
                is_online[int(ids)] = int(time) + 60
            else:
                # get id field, split by space, skip the "id" text and take the number
                # + 1 to that id numbers mentions
                if ids != "HERE" and ids != "ALL":
                    for id in ids.split(" "):
                        id = int(id[2:])
                        mentions[id] += 1
                # if all add 1 to all users
                elif ids == "ALL":
                    for i in range(len(is_online)):
                        mentions[i] += 1
                # increment mention count only for users who are online by checking the time
                else:
                    for i in range(len(is_online)):
                        if is_online[i] <= int(time):
                            mentions[i] += 1
            
        return mentions