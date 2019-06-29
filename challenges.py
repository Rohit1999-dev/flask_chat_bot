from flask import *
import random,json


task = Flask(__name__)
with open("challenges2.json","r") as file:
    all_challenges = json.load(file)
    print(all_challenges)

#getting all the challenges

@task.route("/all_challenges",methods = ["GET"])
def get_all_challenges():
    return jsonify(all_challenges)


# getting a challenge by its # ID

@task.route("/all_challenges/<int:challenge_id>",methods = ["GET"])
def get_a_challenge(challenge_id):
    single =[single for single in all_challenges if single["id"] == challenge_id]
    if len(single)== 0:
        abort(600)
    return jsonify(single)

# # here randomly pic question 


@task.route("/all_challenges/random",methods = ["GET"])
def get_random_challenge():
    string = random.choice(all_challenges)
    return jsonify({"challenge":string["challenge"]})


# ## randomly pic question according level 

@task.route("/all_challenges/random/<level>",methods = ["GET"])
def get_by_level(level):
    by_level = [by_level for by_level in all_challenges if by_level["level"]==level]
    string = random.choice(by_level)

    return jsonify({"challenge":string["challenge"]},{"id":string["id"]})




if __name__=='__main__':
    task.run(debug= True,port=50000)