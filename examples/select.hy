(import [hyenas[*]])
(import [pandas [read_csv]])

(print
    (
        select  :cols [ (count_agg "long_name") (mean_agg "weight_kg")] 
                :from_df (read_csv "/home/lordbertson/Projects/badger/data/players_21.csv") 
                :group_by ["height_cm"]
    )
)