pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'echo Installing dependencies...'
            }
        }

        stage('Run Pipeline') {
            steps {
                sh '''
                echo Running data pipeline...
                mkdir -p parquet_data
                mkdir -p generated_report

                echo "dummy parquet file" > parquet_data/facility_type_avg_time_spent_per_visit_date
                echo "dummy parquet file" > parquet_data/facility_name_min_time_spent_per_visit_date
                echo "dummy parquet file" > parquet_data/patient_sum_treatment_cost_per_facility_type

                echo "<html><body>Report</body></html>" > generated_report/report.html
                '''
            }
        }
    }
}
