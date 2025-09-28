import pandas as pd
import matplotlib.pyplot as plt

def load_data(ghana_file, ivory_file):
    df_ghana = pd.read_csv(ghana_file)
    df_ivory = pd.read_csv(ivory_file)
    return df_ghana, df_ivory

def plot_scatter(df, country_name):
    plt.scatter(df['Year'], df['Yield'], label=f'{country_name} Yield')
    plt.xlabel('Year')
    plt.ylabel('Yield')
    plt.title(f'{country_name} Yield by Year')
    plt.grid(True)
    plt.show()

def plot_bar(df, country_name):
    plt.bar(df['Year'], df['Area harvested'], label=f'{country_name} Area')
    plt.xlabel('Year')
    plt.ylabel('Area harvested')
    plt.title(f'{country_name} Area harvested by Year')
    plt.grid(True)
    plt.show()

def combined_plots(df_ghana, df_ivory):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Ghana scatter
    axs[0,0].scatter(df_ghana['Year'], df_ghana['Yield'], color='green')
    axs[0,0].set_title('Ghana Yield by Year')
    axs[0,0].set_xlabel('Year')
    axs[0,0].set_ylabel('Yield')

    # Ivory scatter
    axs[0,1].scatter(df_ivory['Year'], df_ivory['Yield'], color='brown')
    axs[0,1].set_title('Ivory Coast Yield by Year')
    axs[0,1].set_xlabel('Year')
    axs[0,1].set_ylabel('Yield')

    # Ghana bar
    axs[1,0].bar(df_ghana['Year'], df_ghana['Area harvested'], color='blue')
    axs[1,0].set_title('Ghana Area harvested by Year')
    axs[1,0].set_xlabel('Year')
    axs[1,0].set_ylabel('Area harvested')

    # Ivory bar
    axs[1,1].bar(df_ivory['Year'], df_ivory['Area harvested'], color='orange')
    axs[1,1].set_title('Ivory Coast Area harvested by Year')
    axs[1,1].set_xlabel('Year')
    axs[1,1].set_ylabel('Area harvested')

    fig.suptitle('Cocoa Production in Ghana and Ivory Coast')
    plt.tight_layout()
    plt.savefig('cocoa_production.pdf')
    plt.show()

def main():
    ghana_file = 'ghana_cocoa.csv'
    ivory_file = 'ivorycoast_cocoa.csv'

    df_ghana, df_ivory = load_data(ghana_file, ivory_file)

    # Task 2 plots
    plot_scatter(df_ghana, 'Ghana')
    plot_scatter(df_ivory, 'Ivory Coast')
    plot_bar(df_ghana, 'Ghana')
    plot_bar(df_ivory, 'Ivory Coast')

    # Task 3 and 4: combined plot with titles, labels, saved to PDF
    combined_plots(df_ghana, df_ivory)

if __name__ == "__main__":
    main()
