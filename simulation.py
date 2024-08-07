# # THE PROGRESSIVE ACCEPTANCE OF VACCINATIONS DURING THE COVID-19 CRISES IN BRISTOL

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani

pop = 10000

# set colours for animation representation using RGB tuples
red = (0.96, 0.15, 0.15)  # infected
green = (0, 0.86, 0.03)  # first dose
orange = (0.90, 0.68, 0.18)  # second dose
black = (0, 0, 0)  # third dose
colors = (0.41, 0.70, 0.83) #background

# Define the parameters
COVID_19 = {
    'r0': 2.28,
    'infected': 5,
    'first_dose': 0.7,
    'second_dose': 0.2,
    'third_dose': 0.1,
    'start': 0.034,
    'end': (21, 42),
    'serial_interval': 7,
    'mid': 0.2,
    'mild_rec': (7, 14),
    'half_way': (14, 56)
}


# # Create a class to Hold all functionality
# A class was created to contain several different functions
# The class was first initialized with a sample polar plot with size 5, and certain hypothetical parameters were created
# Real data was tested in the simulation, however, we experienced RunTime errors and the simulation was very slow
# Because we were dealing with a tonne of data

class Vaccine():
    def __init__(self, params):
        '''The class was created to Hold all relevant functions, it was first initialized with a sample polar plot
        with size 5 and certain hypothetical parameters such as the serial_interval (predicting the interval between the spread of the infection
        and the adoption of the vaccines) were used.'''
        ''' The simulation is a realistic video representation of the progressive acceptance of vaccinations during the COVID-19 Crises in Bristol.
         The data set used in this project contained information on the number of doses of vaccines distributed in each region and
         the cumulative number of infections. For Bristol, this was about 150,647, with the ratio of first dose, second and third dose being 7:2:1.
          These data were used in the creation of parameters necessary for building the class in which functions for the simulation were to run.'''

        # params: dictionary with all relevant information
        # create a polar histogram using theta, radii and width (dimensions) instead of x and y

        self.fig = plt.figure()
        # instantiate a polar plot, 111 means a 1 x 1 grid
        self.axes = self.fig.add_subplot(111, projection='polar')
        self.axes.grid(False)
        # modify axes to remove grid lines and tick marks
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        # set the radius of the plot
        self.axes.set_ylim(0, 1)

        # flashing text/annotations.. these would show above and below the polar plot
        # pi is the ratio of a circumference of a circle to its diameter

        self.day_text = self.axes.annotate('Day ', xy=[np.pi / 2, 1], ha='center', va='bottom')
        # centred at the top of the plot... theta value is pi/2 and r value is 1
        # create annotations to show at the bottom of the plot, and the colours of these annotations must correspond
        # with the color grid above
        self.infected_text = self.axes.annotate('Infected: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top', color=red)
        self.first_dose_text = self.axes.annotate('\n First Dose: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top',
                                                  color=green)
        self.second_dose_text = self.axes.annotate('\n\n Second Dose: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top',
                                                   color=orange)
        self.third_dose_text = self.axes.annotate('\n\n\n Third Dose: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top',
                                                  color=black)

        # create member variables for the parameters defined so that they can be called
        # The day, infected and vaccinated persons are initialized at zero so that iterations could make the numbers increase
        self.day = 0
        self.infected_people = 0
        self.first_dose_people = 0
        self.second_dose_people = 0
        self.third_dose_people = 0
        self.r0 = params['r0']
        # r0 is the measurement of the contagiousness of the disease
        self.infected = params['infected']
        self.first_dose = params['first_dose']
        self.second_dose = params['second_dose']
        self.third_dose = params['third_dose']
        self.serial_interval = params['serial_interval']
        self.start = params['start']
        self.mid = params['mid']
        self.end = params['end']
        self.end = params['mild_rec']

        # These parameters would create estimated intervals between when the infection spreads, and when vaccination begins
        self.rate = params['infected'] + params['mild_rec'][0]
        self.rate2 = params['infected'] + params['mild_rec'][1]
        self.rate3 = params['infected'] + params['end'][0]
        self.rate4 = params['infected'] + params['end'][1]
        self.rate5 = params['infected'] + params['half_way'][0]
        self.rate6 = params['infected'] + params['half_way'][1]

        # The code is written in such a way that iterations for an entire year are possible/trackable
        # the thetas and rs dictionaries would become populated with dimensions which would be useful for creating the polar plot
        self.mind = {i: {'thetas': [], 'rs': []} for i in range(self.rate, 365)}
        self.mind2 = {'next_batch': {i: {'thetas': [], 'rs': []} for i in range(self.rate3, 365)},
                      'another_batch': {i: {'thetas': [], 'rs': []} for i in range(self.rate5, 365)}}

        # create a control, 1 person at a time
        # restrictions to the extent to which vaccinations were accepted, the virus/vaccination rates would therefore spread in waves
        # That you are vaccinated does not mean you may not get infected
        self.vaccinated_before = 0
        self.vaccinated_after = 1

        self.first_wave()

    def first_wave(self):
        '''The first_wave() function is responsible for depicting how the infections spread through iterations, after it had been initialized to zero.
        It initializes our plot with the set population of 10,000.
        The GOLDEN SPIRAL METHOD discussed on stackoverflow: https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere was the principle behind the sections witnessed in the polar plot.
        It generates a 2D-spiral algorithm'''
        '''This function initializes our plot with a population of 10,000'''
        # spread of the infection versus vaccine adoption rate
        pop = 10000
        # let us represent the first patient
        self.first_dose_people = 1
        self.infected_people = 1
        # golden spiral method
        indices = np.arange(0, pop) + 0.5
        self.thetas = np.pi * (1 + 5 ** 0.5) * indices
        self.rs = np.sqrt(indices / pop)
        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color=colors)
        # first infected patients color changed to indicate movement
        self.axes.scatter(self.thetas[0], self.rs[0], s=3, color=red)
        self.mind[self.rate]['thetas'].append(self.thetas[0])
        self.mind[self.rate]['rs'].append(self.rs[0])

    # Check polar histogram
    # Vaccine(COVID_19)
    # plt.show()
    # This is to check if the polar histogram has any problems

    # Let us check how the vaccine was disseminated

    def Vaccine_share(self, i):
        '''The Vaccine_share() function would calculate the number of newly infected people while vaccinations are out,
         a serial interval of 7days was used, however, this value can be changed/adjusted. '''
        # calculate the number of newly infected people during vaccine roll
        self.vaccinated_before = self.vaccinated_after
        if self.day % self.serial_interval == 0 and self.vaccinated_before < pop:
            self.new_vaccine = round(self.r0 * self.infected_people)
            # 1.1. means at least 10% of the population are not susceptible to covid, hence they do not get vaccinated
            self.vaccinated_after += round(self.new_vaccine * 1.1)
            # we have to ensure that the exposure and vaccination rates do not exceed the population size we have selected
            if self.vaccinated_after > pop:
                self.new_vaccine = round((pop - self.vaccinated_before) * 0.9)
                self.vaccinated_after = pop

            self.first_dose_people += self.new_vaccine
            self.infected_people += self.new_vaccine

            # randomly select newly vaccinated people and pass in ranges, and replace with False so we dont get the same values multiple times
            self.new_vaccine_indices = list(np.random.choice(range(self.vaccinated_before, self.vaccinated_after),
                                                             self.new_vaccine, replace=False))
            thetas = [self.thetas[i] for i in self.new_vaccine_indices]
            rs = [self.rs[i] for i in self.new_vaccine_indices]

            self.animation.event_source.stop()

            if len(self.new_vaccine_indices) > 24:
                size_list = round(len(self.new_vaccine_indices) / 24)
                # chunks defined?
                theta_chunks = list(self.chunks(thetas, size_list))
                r_chunks = list(self.chunks(rs, size_list))
                self.anim2 = ani.FuncAnimation(self.fig, self.step_by_step,
                                               interval=50, frames=len(theta_chunks),
                                               fargs=(theta_chunks, r_chunks, red))


            else:
                self.anim2 = ani.FuncAnimation(self.fig, self.step_by_step,
                                               interval=50, frames=len(thetas),
                                               fargs=(thetas, rs, red))

            self.Doses()

        self.day += 1
        self.updates()
        self.update_annotation()

    def step_by_step(self, i, thetas, rs, color):
        self.axes.scatter(thetas[i], rs[i], s=5, color=color)
        if i == (len(thetas) - 1):
            self.anim2.event_source.stop()
            self.animation.event_source.start()

    # divide population into chunks of equal size
    def chunks(self, a_list, n):
        for i in range(0, len(a_list), n):
            yield a_list[i:i + n]

    def Doses(self):
        '''calculate the doses given during each wave of the infection'''
        first = round(self.first_dose * self.new_vaccine)
        second = round(self.second_dose * self.new_vaccine)

        # randomly choose a set of indices
        self.first_indices = np.random.choice(self.new_vaccine_indices, first,
                                              replace=False)
        # use list comprehension to get remaining indices
        balance = [
            i for i in self.new_vaccine_indices if i not in self.first_indices
        ]

        # after vaccine dissemination, some people would still fall sick and would be enthusiastic about the third dose
        # this would give us a percentage of successful vaccinations
        checking_work = 1 - (self.start / self.second_dose)
        success = round(checking_work * second)

        # These indices represent those who had severe cases and still remained infectious(fs)
        # and those who even in this state went for third vaccine shot

        self.fs_indices = []
        self.ss_indices = []

        if balance:
            self.fs_indices = np.random.choice(balance, success, replace=False)
            self.ss_indices = [i for i in balance if i not in self.fs_indices]

        '''optimum rate of dissemination of vaccine while infection spreads
        # These are done for positive persons (first indices)
        # persons who have taken the first and second dose and who are still positive (fs indices)
        # Persons who have contracted the disease multiple times but still went to have a third dose (ss indices)'''

        optimum = self.day + self.rate
        optimum1 = self.day + self.rate2
        for each in self.first_indices:
            recovery_day = np.random.randint(optimum, optimum1)
            recovery_theta = self.thetas[each]
            recovery_r = self.rs[each]

            self.mind[recovery_day]['thetas'].append(recovery_theta)
            self.mind[recovery_day]['rs'].append(recovery_r)

        optimum = self.day + self.rate3
        optimum1 = self.day + self.rate4
        for recovery in self.fs_indices:
            recovery_day = np.random.randint(optimum, optimum1)
            recovery_theta1 = self.thetas[recovery]
            recovery_r1 = self.rs[recovery]

            self.mind2['next_batch'][recovery_day]['thetas'].append(recovery_theta1)
            self.mind2['next_batch'][recovery_day]['rs'].append(recovery_r1)

        optimum = self.day + self.rate5
        optimum1 = self.day + self.rate6
        for some in self.ss_indices:
            recovery_day1 = np.random.randint(optimum, optimum1)
            recovery_theta2 = self.thetas[some]
            recovery_r2 = self.rs[some]

            self.mind2['another_batch'][recovery_day1]['thetas'].append(recovery_theta2)
            self.mind2['another_batch'][recovery_day1]['rs'].append(recovery_r2)

    def updates(self):
        '''This would update the color of plot points when infections occur, whether or not they have been vaccinated'''
        if self.day >= self.rate:
            recovery_theta = self.mind[self.day]['thetas']
            recovery_r = self.mind[self.day]['rs']
            self.axes.scatter(recovery_theta, recovery_r, s=5, color=green)
            self.second_dose_people += len(recovery_theta)
            self.first_dose_people -= len(recovery_theta)
        if self.day >= self.rate3:
            recovery_theta1 = self.mind2['next_batch'][self.day]['thetas']
            recovery_r1 = self.mind2['next_batch'][self.day]['rs']
            self.axes.scatter(recovery_theta1, recovery_r1, s=5, color=orange)
            self.second_dose_people += len(recovery_theta1)
            self.first_dose_people -= len(recovery_theta1)
        if self.day >= self.rate5:
            recovery_theta2 = self.mind2['another_batch'][self.day]['thetas']
            recovery_r2 = self.mind2['another_batch'][self.day]['rs']
            self.axes.scatter(recovery_theta2, recovery_r2, s=5, color=black)
            self.third_dose_people += len(recovery_theta2)
            self.first_dose_people -= len(recovery_theta2)

    def update_annotation(self):
        '''The update_annotation function would make changes to the annotations created at the beginning on the polar plot,
         so that each data would change and reflect on the plot. Formatted strings were used to make changes'''
        self.day_text.set_text(f'Day {self.day}')
        self.infected_text.set_text(f'Infected: {self.infected_people}')
        self.first_dose_text.set_text(f'\n First Dose: {self.first_dose}')
        self.second_dose_text.set_text(f'\n\n Second Dose: {self.second_dose}')
        self.third_dose_text.set_text(f'\n\n\n Third Dose: {self.third_dose}')

    def gen(self):
        while self.third_dose_people + self.second_dose_people < self.infected_people:
            yield

    def animate(self):
        '''-The animation would look like a circle, starting with a centralized red dot signifying an infected person
        - The disease would spread, and vaccine adoption rates can be spotted during the proliferation of the disease
        - This does not necessarily mean that infections have reduced/have been curbed
        - The simulation would run until it shows a phase of equilibria between vaccinations and infections
        And then a decline in infectious rates'''
        self.animation = ani.FuncAnimation(self.fig, self.Vaccine_share, frames=self.gen, repeat=True)


def Main_function():
    covid = Vaccine(COVID_19)
    covid.animate()
    plt.show()


if __name__ == '__main__':
    Main_function()

# simulation complete
