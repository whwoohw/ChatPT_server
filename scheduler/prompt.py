
def exercise_prompt(sex, state, purpose, place, body_component, routine, time):
  return f"""I want you to recommend me of workout routine.
    My sex is {sex}.
    My current body state is {state}.
    My purpose of exercising is to {purpose}.
    I usually exercise in {place}.
    My mainly concern area on my body while exercising is {body_component}.
    I exercise {routine}.
    I usually workout for {time}.
    Now, make me the workout routine which contains exercise type name, how much repetition and time that I should take for a set, and how much weight that I need to lift.
    The form of answer should be an JSON.
    'KEYS FOR JSON 1': key values for each of items are day of the week, exercise type name, duration, repetition, weight. 
    and give me the reason why you recommended this routine based on my current state that I mentioned.
    'KEYS FOR JSON 2': key for the reason should be 'reason'.
    'BAD EXAMPLE' : This is an bad example that you have sent to me. 'duration': '3 sets of 10','repetitions': '10'. 
    'VALUES FOR JSON 1' : You should take care of that the repetitions means the number of reps per a set and total number of set. And also that the duration is meant to be a total expected time for completing this exercise.
    'VALUES FOR JSON 2' : You should recommend weight formatted as 'percentage% of 1RM'.
    'VALUES FOR JSON 3' : You should recommend duration of the exercise formatted as 'minute'.
    
  """

meal_plan_form = {
  'meal_plan':[
  {'Monday':[
  {'time':'breakfast', 
   'menu':[{'food':'salad', 'kcal':'50'}, {'food':'milk', 'kcal':'70'}], 
   'nutrition':{'protein':'10g', 'fat':'6g', 'carbonhydrate':'15g'}}]}],
   'reason': 'string'
}

def meal_prompt(sex, state, purpose, place, body_component, routine, time):
  return f"""I want you to recommend me of daily meal plan.
            My sex is {sex}.
            My current body state is {state}.
            My purpose of exercising is to {purpose}.
            Now, make me an daily meal plan of whole week which contains when to eat, such as breakfast, lunch, or dinner. 
            I also want you to include what specific foods that I need to eat, and the calories of them.
            Finally, I want the total carbonhydrate, fat, protein of each meal.
            'KEYS FOR MEAL PLAN': key values for meal plan is 'time': for when to eat, 'menu' : for what to eat, 'kcal' : for calories of them, 'nutrition' : for nutrition information of each meal per 'time'.
            'VALUES FOR MEAL PLAN': you should verify the calories section's value to be kcal.
            and give me the reason why you suggest this meal plan based on my current state that I mentioned. The reason should be seperated with Meal Plan as a different key in JSON.
            you can refer the example form of the response is, {meal_plan_form}.

  """