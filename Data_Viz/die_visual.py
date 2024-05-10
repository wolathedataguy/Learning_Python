from die import Die
import pygal


# Create  a die
die = Die()

# Make  some  rolls, and store the results in a list
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1 ):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the frequencies
hist = pygal.Bar

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of  Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
