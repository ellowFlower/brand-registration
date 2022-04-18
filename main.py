import dataPreprocessing
import dataVisualization

if __name__ == '__main__':
    data_merged = dataPreprocessing.main()
    dataVisualization.create_bar_plot(data_merged)
