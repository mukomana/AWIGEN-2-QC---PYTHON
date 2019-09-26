import pandas as pd


class Instruments:
    # df is data_frame in csv format
    def __init__(self, df):
        # A list of missing value types
        missing_values = ["n/a", "na", "--"]
        # read the csv file
        self.data = pd.read_csv("../resources/data.csv", na_values=missing_values, index_col=None)

    def getAnthropometryData(self):
        anthropometry = self.data[['study_id',
                                   'gene_uni_site_id_correct',
                                   'anth_standing_height',
                                   'anth_weight',
                                   'anth_waist_circumf_1',
                                   'anth_waist_circumf_2',
                                   'anth_waist_circumf',
                                   'anth_hip_circumf_1',
                                   'anth_hip_circumf_2',
                                   'anth_hip_circumf',
                                   'anth_measurementcollector',
                                   'anthropometric_measurements_complete']]
        return anthropometry

    def get_a_phase_1_data(self):
        a_phase_1_data = self.data[['study_id',
                                    'phase_1_site_id_1',
                                    'phase_1_enrolment_date',
                                    'phase_1_gender',
                                    'phase_1_dob_known',
                                    'phase_1_dob',
                                    'phase_1_yob',
                                    'phase_1_age',
                                    'phase_1_unique_site_id',
                                    'phase_1_home_language',
                                    'phase_1_ethnicity',
                                    'ethnolinguistc_available']]
        return a_phase_1_data

    def get_a_cardiometabolic_risk_factors_diabetes(self):
        a_cardiometabolic_risk_factors_diabetes = self.data[['study_id',
                                                             'carf_blood_sugar',
                                                             'carf_diabetes',
                                                             'carf_diabetes_12months',
                                                             'carf_diabetes_treatment',
                                                             'carf_diabetes_treat_now',
                                                             'carf_diabetes_treat',
                                                             'carf_diabetetreat_specify',
                                                             'carf_diabetes_meds_2',
                                                             'carf_diabetes_traditional',
                                                             'carf_diabetes_history',
                                                             'carf_diabetes_mother',
                                                             'carf_diabetes_father',
                                                             'carf_diabetes_brother_1',
                                                             'carf_diabetes_brother_2',
                                                             'carf_diabetes_brother_3',
                                                             'carf_diabetes_brother_4',
                                                             'carf_diabetes_sister_1',
                                                             'carf_diabetes_sister_2',
                                                             'carf_diabetes_sister_3',
                                                             'carf_diabetes_sister_4',
                                                             'carf_diabetes_son_1',
                                                             'carf_diabetes_son_2',
                                                             'carf_diabetes_son_3',
                                                             'carf_diabetes_son_4',
                                                             'carf_daughter_diabetes_1',
                                                             'carf_diabetes_daughter_2',
                                                             'carf_diabetes_daughter_3',
                                                             'carf_diabetes_daughter_4',
                                                             'carf_diabetes_fam_other',
                                                             'carf_diabetes_fam_specify']]
        return a_cardiometabolic_risk_factors_diabetes

    def get_a_cognition_one(self):
        a_cognition_one = self.data[['study_id',
                                     'cogn_read_sentence',
                                     'cogn_memory',
                                     'cogn_difficulty_remember',
                                     'cogn_difficulty_concern',
                                     'cogn_learning_new_task',
                                     'cogn_word_recall_p1',
                                     'cogn_words_remember_p1',
                                     'cogn_imm_recall_score_p1',
                                     'cogn_year',
                                     'cogn_what_is_the_month',
                                     'cogn_day_of_the_month',
                                     'cogn_country_of_residence',
                                     'cogn_district_province',
                                     'cogn_village_town_city',
                                     'cogn_weekdays_forward',
                                     'cogn_weekdays_backwards',
                                     'cogn_orientation_score']]
        return a_cognition_one

    def get_a_general_health_cancer(self):
        a_general_health_cancer = self.data[['study_id',
                                             'genh_breast_cancer',
                                             'genh_breast_cancer_treat',
                                             'genh_bre_cancer_treat_now',
                                             'genh_breast_cancer_meds',
                                             'genh_bre_cancer_trad_med',
                                             'genh_cervical_cancer',
                                             'genh_cer_cancer_treat',
                                             'genh_cer_cancer_treat_now',
                                             'genh_cervical_cancer_meds',
                                             'genh_cer_cancer_trad_med',
                                             'genh_prostate_cancer',
                                             'genh_pro_cancer_treat',
                                             'genh_pro_cancer_treat_now',
                                             'genh_prostate_cancer_meds',
                                             'genh_pro_cancer_trad_med',
                                             'genh_oesophageal_cancer',
                                             'genh_oes_cancer_treat',
                                             'genh_oes_cancer_treat_now',
                                             'genh_oes_cancer_meds',
                                             'genh_oesophageal_trad_med',
                                             'genh_other_cancers',
                                             'genh_cancer_specify_other',
                                             'genh_other_cancer_treat',
                                             'genh_oth_cancer_treat_now',
                                             'genh_other_cancer_meds',
                                             'genh_oth_cancer_trad_med']]
        return a_general_health_cancer

    def get_a_microbiome(self):
        a_microbiome = self.data[['study_id',
                                  'micr_take_antibiotics',
                                  'micr_diarrhea_last_time',
                                  'micr_worm_intestine_treat',
                                  'micr_probiotics_t_period',
                                  'micr_wormintestine_period',
                                  'micr_probiotics_taken']]
        return a_microbiome

    def get_a_respiratory_health(self):
        a_respiratory_health = self.data[['study_id',
                                          'resp_lung_fnc_symptoms',
                                          'resp_breath_shortness',
                                          'resp_breath_shortness_ever',
                                          'resp_mucus',
                                          'resp_breath_too_short',
                                          'resp_cough',
                                          'resp_wheezing_whistling',
                                          'resp_asthma_diagnosed',
                                          'resp_age_diagnosed',
                                          'resp_asthma_treat',
                                          'resp_asthma_treat_now',
                                          'resp_copd_suffer',
                                          'resp_copd_treat',
                                          'resp_inhaled_medication',
                                          'resp_medication_list',
                                          'resp_puffs_time',
                                          'resp_puffs_times_day',
                                          'resp_measles_suffer']]
        return a_respiratory_health

    def get_b_blood_collection(self):
        b_blood_collection = self.data[['study_id',
                                        'bloc_last_eat_time',
                                        'bloc_last_ate_hrs',
                                        'bloc_last_drink_time',
                                        'bloc_hours_last_drink',
                                        'bloc_fasting_confirmed',
                                        'bloc_two_red_tubes',
                                        'bloc_red_tubes_num',
                                        'bloc_one_purple_tube',
                                        'bloc_if_no_purple_tubes',
                                        'bloc_one_grey_tube',
                                        'bloc_grey_tubes_no',
                                        'bloc_phlebotomist_name',
                                        'bloc_blood_taken_date',
                                        'bloc_bloodcollection_time']]
        return b_blood_collection

    def get_b_cardiometabolic_risk_factors_heart_conditions(self):
        b_cardiometabolic_risk_factors_heart_conditions = self.data[['study_id',
                                                                     'carf_stroke',
                                                                     'carf_stroke_diagnosed',
                                                                     'carf_tia',
                                                                     'carf_weakness',
                                                                     'carf_numbness',
                                                                     'carf_blindness',
                                                                     'carf_half_vision_loss',
                                                                     'carf_understanding_loss',
                                                                     'carf_expression_loss',
                                                                     'carf_angina',
                                                                     'carf_angina_treatment',
                                                                     'carf_angina_treat_now',
                                                                     'carf_angina_meds',
                                                                     'carf_angina_traditional',
                                                                     'carf_pain',
                                                                     'carf_pain2',
                                                                     'carf_pain_action_stopslow',
                                                                     'carf_relief_standstill',
                                                                     'carf_pain_location',
                                                                     'carf_heartattack',
                                                                     'carf_heartattack_treat',
                                                                     'carf_heartattack_meds',
                                                                     'carf_heartattack_trad',
                                                                     'carf_congestiv_heart_fail',
                                                                     'carf_chf_treatment',
                                                                     'carf_chf_treatment_now',
                                                                     'carf_chf_meds',
                                                                     'carf_chf_traditional']]
        return b_cardiometabolic_risk_factors_heart_conditions

    def get_b_frailty_measurements(self):
        b_frailty_measurements = self.data[['study_id',
                                            'frai_standing_up_time',
                                            'frai_use_hands',
                                            'frai_sit_stands_completed',
                                            'frai_comment',
                                            'frai_non_dominant_hand',
                                            'frai_dynometer_force_1',
                                            'frai_dynometer_force_2',
                                            'frai_dynometer_force_3',
                                            'frai_complete_procedure',
                                            'frai_comment_why',
                                            'frai_turn_walk_back',
                                            'frai_need_support',
                                            'frai_procedure_walk_comp',
                                            'frai_please_comment_why']]
        return b_frailty_measurements

    def get_b_general_health_family_history(self):
        b_general_health_family_history = self.data[['study_id',
                                                     'genh_obesity_mom',
                                                     'genh_h_blood_pressure_mom',
                                                     'genh_h_cholesterol_mom',
                                                     'genh_breast_cancer_mom',
                                                     'genh_cervical_cancer_mom',
                                                     'genh_oes_cancer_mom',
                                                     'genh_cancer_other_mom',
                                                     'genh_asthma_mom',
                                                     'genh_obesity_dad',
                                                     'genh_h_blood_pressure_dad',
                                                     'genh_h_cholesterol_dad',
                                                     'genh_prostate_cancer_dad',
                                                     'genh_other_cancers_dad',
                                                     'genh_asthma_dad']]
        return b_general_health_family_history

    def get_b_spirometry_eligibility(self):
        b_spirometry_eligibility = self.data[['study_id',
                                              'rspe_major_surgery',
                                              'rspe_chest_pain',
                                              'rspe_coughing_blood',
                                              'rspe_acute_retinal_detach',
                                              'rspe_any_pain',
                                              'rspe_diarrhea',
                                              'rspe_high_blood_pressure',
                                              'rspe_tb_diagnosed',
                                              'rspe_tb_treat_past4wks',
                                              'rspe_infection',
                                              'rspe_participation',
                                              'rspe_wearing_tightclothes',
                                              'rspe_wearing_dentures',
                                              'rspe_participation_note',
                                              'rspe_researcher_question']]
        return b_spirometry_eligibility

    def get_blood_pressure_and_pulse_measurements(self):
        blood_pressure_and_pulse_measurements = self.data[['study_id',
                                                           'bppm_systolic_1',
                                                           'bppm_diastolic_1',
                                                           'bppm_pulse_1',
                                                           'bppm_measurement_time_1',
                                                           'bppm_systolic_2',
                                                           'bppm_diastolic_2',
                                                           'bppm_pulse_2',
                                                           'bppm_measurement_time_2',
                                                           'bppm_systolic_3',
                                                           'bppm_diastolic_3',
                                                           'bppm_pulse_3',
                                                           'bppm_measurement_time_3',
                                                           'bppm_measurementcollector',
                                                           'bppm_systolic_avg',
                                                           'bppm_diastolic_avg',
                                                           'bppm_pulse_avg']]
        return blood_pressure_and_pulse_measurements

    def c_cardiometabolic_risk_factors_hypertension_choles(self):
        c_cardiometabolic_risk_factors_hypertension_choles = self.data[['study_id',
                                                                        'carf_bp_measured',
                                                                        'carf_hypertension',
                                                                        'carf_hypertension_12mnths',
                                                                        'carf_hypertension_treat',
                                                                        'carf_hypertension_meds',
                                                                        'carf_hypertension_medlist',
                                                                        'carf_hypertension_trad',
                                                                        'carf_cholesterol',
                                                                        'carf_h_cholesterol',
                                                                        'carf_chol_treatment',
                                                                        'carf_chol_treatment_now',
                                                                        'carf_chol_treat_specify',
                                                                        'carf_chol_medicine',
                                                                        'carf_chol_traditional']]
        return c_cardiometabolic_risk_factors_hypertension_choles

    def get_c_cognition_two(self):
        c_cognition_two = self.data[['study_id',
                                     'cogn_delayed_recall_note',
                                     'cogn_delayed_recall',
                                     'cogn_delayed_recall_score',
                                     'cogn_word_cognition_note',
                                     'cogn_word_cognition_list',
                                     'cogn_recognition_score',
                                     'cogn_different_animals',
                                     'cogn_comments']]
        return c_cognition_two

    def get_c_general_health_diet(self):
        c_general_health_diet = self.data[['study_id',
                                           'genh_days_fruit',
                                           'genh_fruit_servings',
                                           'genh_days_veg',
                                           'genh_veg_servings',
                                           'genh_starchy_staple_food',
                                           'genh_starchy_staple_freq',
                                           'genh_staple_servings',
                                           'genh_vendor_meals',
                                           'genh_sugar_drinks',
                                           'genh_juice',
                                           'genh_change_diet',
                                           'genh_lose_weight']]
        return c_general_health_diet

    def get_c_spirometry_test(self):
        c_spirometry_test = self.data[['study_id',
                                       'spiro_eligible',
                                       'spiro_researcher',
                                       'spiro_num_of_blows',
                                       'spiro_num_of_vblows',
                                       'spiro_pass',
                                       'spiro_comment']]
        return c_spirometry_test

    def get_c_urine_collection(self):
        c_urine_collection = self.data[['study_id',
                                        'bloc_urine_collected',
                                        'bloc_specify_reason',
                                        'bloc_urcontainer_batchnum',
                                        'bloc_urine_tube_expiry',
                                        'bloc_urine_collector',
                                        'bloc_urine_taken_date',
                                        'bloc_urinecollection_time']]
        return c_urine_collection

    def get_civil_status_marital_status_education_employment(self):
        civil_status_marital_status_education_employment = self.data[['study_id',
                                                                      'mari_marital_status',
                                                                      'educ_highest_level',
                                                                      'educ_highest_years',
                                                                      'educ_formal_years',
                                                                      'empl_status',
                                                                      'empl_days_work']]
        return civil_status_marital_status_education_employment

    def get_completion_of_questionnaire(self):
        completion_of_questionnaire = self.data[['study_id',
                                                 'comp_sections_1_13',
                                                 'comp_comment_no_1_13',
                                                 'comp_section_14',
                                                 'comp_comment_no_14',
                                                 'comp_section_15',
                                                 'comp_comment_no_15',
                                                 'comp_section_16',
                                                 'comp_comment_no_16',
                                                 'comp_section_17',
                                                 'comp_comment_no_17',
                                                 'comp_section_18',
                                                 'comp_comment_no_18',
                                                 'comp_section_19',
                                                 'comp_comment_no_19',
                                                 'comp_section_20',
                                                 'comp_comment_no_20']]
        return completion_of_questionnaire

    def get_d_cardiometabolic_risk_factors_kidney_thyroid_ra(self):
        d_cardiometabolic_risk_factors_kidney_thyroid_ra = self.data[['study_id',
                                                                      'carf_thyroid',
                                                                      'carf_thyroid_type',
                                                                      'carf_thryroid_specify',
                                                                      'carf_thyroid_treatment',
                                                                      'carf_thyroid_treat_use',
                                                                      'carf_parents_thyroid',
                                                                      'carf_thyroidparnt_specify',
                                                                      'carf_kidney_disease',
                                                                      'carf_kidney_disease_known',
                                                                      'carf_kidneydiseas_specify',
                                                                      'carf_kidney_function_low',
                                                                      'carf_kidney_family',
                                                                      'carf_kidney_family_mother',
                                                                      'carf_kidney_family_father',
                                                                      'carf_kidney_family_other',
                                                                      'carf_kidney_fam_specify',
                                                                      'carf_kidney_family_type',
                                                                      'carf_kidney_fam_tspecify',
                                                                      'carf_joints_swollen_pain',
                                                                      'carf_joints_swollen',
                                                                      'carf_joints_involved',
                                                                      'carf_when_they_hurt',
                                                                      'carf_symptoms_how_long',
                                                                      'carf_arthritis_results',
                                                                      'carf_rheumatoid_factor',
                                                                      'carf_acpa',
                                                                      'carf_esr_crp']]
        return d_cardiometabolic_risk_factors_kidney_thyroid_ra

    def get_d_general_health_exposure_to_pesticides_pollutants(self):
        d_general_health_exposure_to_pesticides_pollutants = self.data[['study_id',
                                                                        'genh_pesticide',
                                                                        'genh_pesticide_years',
                                                                        'genh_pesticide_region',
                                                                        'genh_pesticide_type',
                                                                        'genh_pesticide_list',
                                                                        'genh_cooking_place',
                                                                        'genh_cookingplace_specify',
                                                                        'genh_cooking_done_inside',
                                                                        'genh_energy_source_type',
                                                                        'genh_energy_specify',
                                                                        'genh_smoker_in_your_house',
                                                                        'genh_smoke_freq_someone',
                                                                        'genh_insect_repellent_use']]
        return d_general_health_exposure_to_pesticides_pollutants

    def get_d_reversibility_test(self):
        d_reversibility_test = self.data[['study_id',
                                          'rspir_salb_admin',
                                          'rspir_salb_time_admin',
                                          'rspir_time_started',
                                          'rspir_researcher',
                                          'rspir_num_of_blows',
                                          'rspir_num_of_vblows',
                                          'rspir_comment']]
        return d_reversibility_test

    def get_ethnolinguistic_information(self):
        ethnolinguistic_information = self.data[['study_id',
                                                 'ethn_father_ethn_sa',
                                                 'ethn_father_ethn_ot',
                                                 'ethn_father_lang_sa',
                                                 'ethn_father_lang_ot',
                                                 'ethn_pat_gfather_ethn_sa',
                                                 'ethn_pat_gfather_ethn_ot',
                                                 'ethn_pat_gfather_lang_sa',
                                                 'ethn_pat_gfather_lang_ot',
                                                 'ethn_pat_gmother_ethn_sa',
                                                 'ethn_pat_gmother_ethn_ot',
                                                 'ethn_pat_gmother_lang_sa',
                                                 'ethn_pat_gmother_lang_ot',
                                                 'ethn_mother_ethn_sa',
                                                 'ethn_mother_ethn_ot',
                                                 'ethn_mother_lang_sa',
                                                 'ethn_mother_lang_ot',
                                                 'ethn_mat_gfather_ethn_sa',
                                                 'ethn_mat_gfather_ethn_ot',
                                                 'ethn_mat_gfather_lang_sa',
                                                 'ethn_mat_gfather_lang_ot',
                                                 'ethn_mat_gmother_ethn_sa',
                                                 'ethn_mat_gmother_ethn_ot',
                                                 'ethn_mat_gmother_lang_sa',
                                                 'ethn_mat_gmother_lang_ot']]
        return ethnolinguistic_information

    def get_family_composition(self):
        family_composition = self.data[['study_id',
                                        'famc_siblings',
                                        'famc_number_of_brothers',
                                        'famc_living_brothers',
                                        'famc_number_of_sisters',
                                        'famc_living_sisters',
                                        'famc_children',
                                        'famc_bio_sons',
                                        'famc_living_bio_sons',
                                        'famc_bio_daughters',
                                        'famc_living_bio_daughters']]
        return family_composition

    def get_household_attributes(self):
        household_attributes = self.data[['study_id',
                                          'hous_household_size',
                                          'hous_number_of_rooms',
                                          'hous_number_of_bedrooms',
                                          'hous_electricity',
                                          'hous_solar_energy',
                                          'hous_power_generator',
                                          'hous_alter_power_src',
                                          'hous_television',
                                          'hous_radio',
                                          'hous_motor_vehicle',
                                          'hous_motorcycle',
                                          'hous_bicycle',
                                          'hous_refrigerator',
                                          'hous_washing_machine',
                                          'hous_sewing_machine',
                                          'hous_telephone',
                                          'hous_mobile_phone',
                                          'hous_microwave',
                                          'hous_dvd_player',
                                          'hous_satellite_tv_or_dstv',
                                          'hous_computer_or_laptop',
                                          'hous_internet_by_computer',
                                          'hous_internet_by_m_phone',
                                          'hous_electric_iron',
                                          'hous_fan',
                                          'hous_electric_gas_stove',
                                          'hous_kerosene_stove',
                                          'hous_plate_gas',
                                          'hous_electric_plate',
                                          'hous_torch',
                                          'hous_gas_lamp',
                                          'hous_kerosene_lamp',
                                          'hous_toilet_facilities',
                                          'hous_portable_water',
                                          'hous_grinding_mill',
                                          'hous_table',
                                          'hous_sofa',
                                          'hous_wall_clock',
                                          'hous_bed',
                                          'hous_mattress',
                                          'hous_blankets',
                                          'hous_cattle',
                                          'hous_other_livestock',
                                          'hous_poultry',
                                          'hous_tractor',
                                          'hous_plough']]
        return household_attributes

    def get_infection_history(self):
        infection_history = self.data[['study_id',
                                       'infh_malaria',
                                       'infh_malaria_month',
                                       'infh_malaria_area',
                                       'infh_tb',
                                       'infh_tb_12months',
                                       'infh_tb_diagnosed',
                                       'infh_tb_treatment',
                                       'infh_tb_meds',
                                       'infh_tb_counselling',
                                       'infh_tb_traditional_med',
                                       'infh_hiv_que_answering',
                                       'infh_hiv_tested',
                                       'infh_hiv_status',
                                       'infh_hiv_positive',
                                       'infh_hiv_diagnosed',
                                       'infh_hiv_medication',
                                       'infh_hiv_treatment',
                                       'infh_hiv_arv_meds',
                                       'infh_hiv_arv_meds_now',
                                       'infh_hiv_arv_meds_specify',
                                       'infh_hiv_arv_single_pill',
                                       'infh_hiv_pill_size',
                                       'infh_hiv_traditional_meds',
                                       'infh_painful_feet_hands',
                                       'infh_hypersensitivity',
                                       'infh_kidney_problems',
                                       'infh_liver_problems',
                                       'infh_change_in_body_shape',
                                       'infh_mental_state_change',
                                       'infh_chol_levels_change',
                                       'infh_hiv_test',
                                       'infh_hiv_counselling']]
        return infection_history

    def get_participant_identification(self):
        participant_identification = self.data[['study_id',
                                                'gene_site_id',
                                                'gene_uni_site_id_correct',
                                                'gene_site',
                                                'gene_enrolment_date',
                                                'gene_start_time',
                                                'gene_end_time',
                                                'gene_compensation',
                                                'demo_approx_dob_is_correct',
                                                'demo_dob_is_correct',
                                                'demo_date_of_birth_known',
                                                'demo_dob_new',
                                                'demo_approx_dob_new',
                                                'test',
                                                'demo_date_of_birth',
                                                'demo_age_at_collection',
                                                'demo_gender_is_correct',
                                                'demo_gender_correction',
                                                'demo_gender',
                                                'home_language_confirmation',
                                                'home_language',
                                                'other_home_language',
                                                'demo_home_language',
                                                'ethnicity_confirmation',
                                                'ethnicity',
                                                'other_ethnicity',
                                                'gene_identity_confirmed']]
        return participant_identification

    def get_physical_activity_and_sleep(self):
        physical_activity_and_sleep = self.data[['study_id',
                                                 'gpaq_gpaq_notes'
                                                 'gpaq_work_days'
                                                 'gpaq_work_weekend'
                                                 'gpaq_phy_activity_notes'
                                                 'gpaq_work_sedentary'
                                                 'gpaq_work_vigorous'
                                                 'gpaq_work_vigorous_days'
                                                 'gpaq_work_vigorous_time'
                                                 'gpaq_work_vigorous_hrs'
                                                 'gpaq_work_vigorous_mins'
                                                 'gpaq_work_moderate'
                                                 'gpaq_work_moderate_days'
                                                 'gpaq_work_moderate_time'
                                                 'gpaq_work_moderate_hrs'
                                                 'gpaq_work_moderate_mins'
                                                 'gpaq_work_day_time'
                                                 'gpaq_work_day_hrs'
                                                 'gpaq_work_day_mins'
                                                 'gpaq_travel_notes'
                                                 'gpaq_transport_phy'
                                                 'gpaq_transport_phy_days'
                                                 'gpaq_transport_phy_time'
                                                 'gpaq_transport_phy_hrs'
                                                 'gpaq_transport_phy_mins'
                                                 'gpaq_leisure_phy'
                                                 'gpaq_leisure_vigorous'
                                                 'gpaq_leisurevigorous_days'
                                                 'gpaq_leisurevigorous_time'
                                                 'gpaq_leisurevigorous_hrs'
                                                 'gpaq_leisurevigorous_mins'
                                                 'gpaq_leisuremoderate'
                                                 'gpaq_leisuremoderate_days'
                                                 'gpaq_leisuremoderate_time'
                                                 'gpaq_leisuremoderate_hrs'
                                                 'gpaq_leisuremoderate_mins'
                                                 'gpaq_work_day_stng_time'
                                                 'gpaq_work_day_stng_hrs'
                                                 'gpaq_work_day_stng_mins'
                                                 'gpaq_non_work_day_time'
                                                 'gpaq_non_work_day_hrs'
                                                 'gpaq_non_work_day_mins'
                                                 'gpaq_week_sleep_time'
                                                 'gpaq_week_wakeup_time'
                                                 'gpaq_weekend_sleep_time'
                                                 'gpaq_weekend_wakeup_time'
                                                 'gpaq_sleep_room_pple_num'
                                                 'gpaq_sleep_room_livestock'
                                                 'gpaq_sleep_on'
                                                 'gpaq_mosquito_net_use'
                                                 'gpaq_feel_alert'
                                                 'gpaq_sleeping_difficulty'
                                                 'gpaq_difficulty_staysleep'
                                                 'gpaq_waking_early_problem'
                                                 'gpaq_waking_up_tired'
                                                 'gpaq_sleep_pattern_satis'
                                                 'gpaq_sleep_interfere']]
        return physical_activity_and_sleep

    def get_point_of_care_testing(self):
        point_of_care_testing = self.data[['study_id',
                                           'poc_test_conducted',
                                           'poc_comment',
                                           'poc_instrument_serial_num',
                                           'poc_test_strip_batch_num',
                                           'poc_teststrip_expiry_date',
                                           'poc_test_date',
                                           'poc_test_time',
                                           'poc_researcher_name',
                                           'poc_glucose_test_result',
                                           'poc_chol_result',
                                           'poc_gluc_results_provided',
                                           'poc_gluc_results_notes',
                                           'poc_chol_results_provided',
                                           'poc_chol_results_notes',
                                           'poc_glucresults_discussed',
                                           'poc_cholresults_discussed',
                                           'poc_seek_advice',
                                           'poc_hiv_test_conducted',
                                           'poc_hiv_comment',
                                           'poc_hiv_pre_test',
                                           'poc_pre_test_worker',
                                           'poc_test_kit_serial_num',
                                           'poc_hiv_strip_batch_num',
                                           'poc_hiv_strip_expiry_date',
                                           'poc_hiv_test_date_done',
                                           'poc_technician_name',
                                           'poc_hiv_test_result',
                                           'poc_result_provided',
                                           'poc_post_test_counselling',
                                           'poc_post_test_worker',
                                           'poc_hivpositive_firsttime',
                                           'poc_hiv_seek_advice']]
        return point_of_care_testing

    def get_pregnancy_and_menopause(self):
        pregnancy_and_menopause = self.data[['study_id',
                                             'preg_pregnant',
                                             'preg_alert',
                                             'preg_num_of_pregnancies',
                                             'preg_num_of_live_births',
                                             'preg_birth_control',
                                             'preg_hysterectomy',
                                             'preg_regular_periods',
                                             'preg_last_period_remember',
                                             'preg_last_period',
                                             'preg_last_period_mon',
                                             'preg_last_period_mon_2',
                                             'preg_period_more_than_yr']]
        return pregnancy_and_menopause

    def get_substance_use(self):
        substance_use = self.data[['study_id',
                                   'subs_tobacco_use',
                                   'subs_smoke_100',
                                   'subs_smoke_now',
                                   'subs_smoke_last_hour',
                                   'subs_smoke_cigarettes',
                                   'subs_smoke_specify',
                                   'subs_smoking_frequency',
                                   'subs_smoke_per_day',
                                   'subs_smoking_start_age',
                                   'subs_smoking_stop_year',
                                   'subs_smokeless_tobacc_use',
                                   'subs_snuff_use',
                                   'subs_snuff_method_use',
                                   'subs_snuff_use_freq',
                                   'subs_freq_snuff_use',
                                   'subs_tobacco_chew_use',
                                   'subs_tobacco_chew_freq',
                                   'subs_tobacco_chew_d_freq']]
        return substance_use

    def get_trauma(self):
        trauma = self.data[['study_id',
                            'tram_experienced_events',
                            'tram_injury_ill_assault',
                            'tram_relative_ill_injured',
                            'tram_deceased',
                            'tram_family_friend_died',
                            'tram_marital_separation',
                            'tram_broke_relationship',
                            'tram_problem_with_friend',
                            'tram_unemployed',
                            'tram_sacked_from_your_job',
                            'tram_financial_crisis',
                            'tram_problems_with_police',
                            'tram_some_valued_lost']]
        return trauma

    def get_ultrasound_and_dxa_measurements(self):
        ultrasound_and_dxa_measurements = self.data[['study_id',
                                                     'ultr_vat_scat_measured',
                                                     'ultr_comment',
                                                     'ultr_technician',
                                                     'ultr_visceral_fat',
                                                     'ultr_subcutaneous_fat',
                                                     'ultr_cimt',
                                                     'ultr_cimt_comment',
                                                     'ultr_cimt_technician',
                                                     'ultr_cimt_right_min',
                                                     'ultr_cimt_right_max',
                                                     'ultr_cimt_right_mean',
                                                     'ultr_cimt_left_min',
                                                     'ultr_cimt_left_max',
                                                     'ultr_cimt_left_mean',
                                                     'ultr_plaque',
                                                     'ultr_plaque_comment',
                                                     'ultr_plaque_technician',
                                                     'ultr_plaque_present',
                                                     'ultr_plaque_right_min',
                                                     'ultr_plaque_right_max',
                                                     'ultr_plaque_right_mean',
                                                     'ultr_plaque_left_min',
                                                     'ultr_plaque_left_max',
                                                     'ultr_plaque_left_mean',
                                                     'ultr_dxa_scan_completed',
                                                     'ultr_dxa_scan_comment',
                                                     'ultr_dxa_measurement_1',
                                                     'ultr_dxa_measurement_2',
                                                     'ultr_dxa_measurement_3',
                                                     'ultr_dxa_measurement_4',
                                                     'ultr_dxa_measurement_5']]
        return ultrasound_and_dxa_measurements
