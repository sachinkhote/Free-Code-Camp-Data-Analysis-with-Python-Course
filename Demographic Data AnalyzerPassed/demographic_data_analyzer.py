import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')
  race_count = df['race'].value_counts()
  men = df.loc[df['sex'] == 'Male', 'age']
  average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?
  bachelor = df['education'] == 'Bachelors'
  percentage_bachelors = round(
      bachelor.sum() * 100 / df['education'].value_counts().sum(), 1)
  master = df['education'] == 'Masters'
  doctor = df['education'] == 'Doctorate'

  higher = (bachelor) | (master) | (doctor)
  lower = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (
      df['education'] != 'Doctorate')
  higher_education = None
  lower_education = None
  hi_ed_rich_number = df.loc[higher
                             & (df['salary'] == '>50K')].value_counts().sum()
  hi_ed_total = df.loc[higher].value_counts().sum()
  #print(hi_ed_total)
  higher_education_rich = round(hi_ed_rich_number * 100 / hi_ed_total, 1)

  low_ed_rich_number = df.loc[lower
                              & (df['salary'] == '>50K')].value_counts().sum()
  low_ed_total = df.loc[lower].value_counts().sum()
  #print(low_ed_total)
  lower_education_rich = round(low_ed_rich_number * 100 / low_ed_total, 1)
  min_work_hours = df['hours-per-week'].min()
  num_min_workers = df.loc[df['hours-per-week'] == 1].value_counts().sum()

  min_workers_rich = df.loc[(df['hours-per-week'] == 1)
                            & (df['salary'] == '>50K')].value_counts().sum()
  #print('WORK LESS BUT RICH', min_workers_rich)

  rich_percentage = round(min_workers_rich * 100 / num_min_workers, 1)

  country_population = df['native-country'].value_counts()
  rich_pop_by_country = df.loc[df['salary'] == '>50K',
                               'native-country'].value_counts()
  percent_rich_by_country = round(
      rich_pop_by_country * 100 / country_population, 1)
  highest_earning_country = percent_rich_by_country.idxmax()
  highest_earning_country_percentage = percent_rich_by_country.max()

  india = df['native-country'] == 'India'
  india_rich = df.loc[(india) & (df['salary'] == '>50K')]
  india_occ_rich = india_rich['occupation'].value_counts().idxmax()
  top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
