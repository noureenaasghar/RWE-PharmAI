
import streamlit as st
import json
from groq import Groq

st.set_page_config(
    page_title="RWE-PharmAI",
    page_icon="🔬",
    layout="wide"
)

proposal_data = json.loads('{"Title": "Association of GLP-1 Receptor Agonist Use With Alcohol-Related Health Outcomes Among Adults With Alcohol Use Disorder and Type 2 Diabetes", "Research Question": "Among adults with Alcohol Use Disorder and Type 2 Diabetes, is GLP-1 receptor agonist use associated with a lower risk of alcohol-related emergency department visits and hospitalizations compared with DPP-4 inhibitor use?", "Study Design": "Retrospective Cohort Study", "Target Population": {"age": "18 years or older", "required_conditions": ["Alcohol Use Disorder (AUD)", "Type 2 Diabetes (T2D)"], "exposure_group": {"medication": "GLP-1 receptor agonists", "design": "New users"}, "comparator_group": {"medication": "DPP-4 inhibitors", "design": "New users"}, "washout_period": "12 months before index date", "index_date": "First eligible medication initiation", "status": "Provisional; requires literature and data validation"}, "Eligibility": {"Inclusion": ["Age 18 years or older at index date", "AUD documented before index date", "T2D documented before index date", "Initiation of GLP-1 RA or DPP-4 inhibitor", "No GLP-1 RA or DPP-4 inhibitor use during the 12-month washout", "Available baseline healthcare records"], "Exclusion": ["Age below 18 years", "No documented AUD before index date", "No documented T2D before index date", "Prior GLP-1 RA or DPP-4 inhibitor use during washout", "Type 1 Diabetes diagnosis (E10.-) without confirmed T2D eligibility", "Insufficient medication or baseline records"]}, "Exposure": {"exposure_group": "New users of GLP-1 receptor agonists", "medication_evidence": ["Prescription records", "Dispensing records, if available"], "index_date": "First eligible medication initiation", "comparator_group": "New users of DPP-4 inhibitors", "limitation": "Prescription or dispensing does not confirm actual medication use"}, "Comparator": {"population": "Adults with AUD and T2D", "medication": "DPP-4 inhibitors", "design": "New users", "index_date": "First eligible DPP-4 inhibitor initiation", "washout": "No GLP-1 RA or DPP-4 inhibitor use during the preceding 12 months"}, "Primary Outcomes": {"ED_visits": {"encounter_requirement": "Documented Emergency Department encounter", "diagnosis_requirement": "Alcohol-related diagnosis during encounter", "measurement_period": "Up to 12 months after index date", "status": "Encounter and diagnosis validation pending"}, "Hospitalizations": {"encounter_requirement": "Documented inpatient hospital admission", "diagnosis_requirement": "Alcohol-related diagnosis during admission", "measurement_period": "Up to 12 months after index date", "status": "Encounter and diagnosis validation pending"}}, "Statistical Analysis": {"descriptive_analysis": ["Mean and standard deviation or median and IQR", "Frequencies and percentages", "Baseline characteristics by treatment group"], "primary_analysis": {"binary_outcomes": "Modified Poisson regression with robust standard errors", "effect_measure": "Adjusted Risk Ratio with 95% Confidence Interval"}, "secondary_analysis": {"recurrent_event_counts": "Negative binomial regression if overdispersion is present", "effect_measure": "Incidence Rate Ratio with 95% Confidence Interval"}, "confounding_control": ["Multivariable adjustment", "Propensity score methods, subject to data suitability"], "significance_level": "Two-sided p < 0.05", "status": "Proposed; final methods depend on data structure and assumptions"}, "Confounders": {"demographics": ["Age", "Sex"], "diabetes_related": ["Diabetes duration", "Diabetes complications", "HbA1c, if available"], "AUD_related": ["AUD history", "AUD severity indicators", "Previous alcohol-related encounters"], "clinical_conditions": ["Obesity", "Liver disease", "Psychiatric comorbidities"], "healthcare_and_treatment": ["Prior ED visits and hospitalizations", "Relevant medication use", "Insurance or healthcare access indicators, if available"]}, "Pending Validation": {"provisionally_defined": ["Study design and PICO", "Target population and eligibility criteria", "GLP-1 RA exposure and DPP-4 comparator", "Index date alignment", "12-month baseline and washout periods", "12-month follow-up", "Primary and secondary outcomes", "Censoring rules", "Missing data assessment plan", "Confounder framework", "Statistical analysis strategy", "Propensity score balance assessment", "Sensitivity analysis framework"], "requires_literature_or_code_validation": ["AUD diagnosis coding algorithm", "Type 2 diabetes diagnosis coding algorithm", "Alcohol-related ED and hospitalization code lists", "Medication exposure identification rules", "Clinical justification for DPP-4 comparator", "Outcome definition and measurement validity"], "requires_actual_data": ["Eligible patient numbers and sample size assessment", "Availability and completeness of baseline variables", "Outcome event frequency", "Propensity score overlap and matching feasibility", "Missing data patterns", "Final statistical model selection"]}}')

st.title("RWE-PharmAI")
st.subheader("AI-Assisted Real-World Evidence Research Framework")

st.info(
    "Research-support prototype. AI outputs require expert review "
    "and do not represent validated clinical findings."
)

api_key = st.secrets.get("GROQ_API_KEY", "")

if not api_key:
    st.error("Groq API Key is missing. Please configure it in Streamlit Secrets.")
    st.stop()

tab1, tab2, tab3 = st.tabs([
    "Research Proposal",
    "AI Research Review",
    "Gap Prioritization"
])

with tab1:
    st.header("Research Proposal")
    st.json(proposal_data, expanded=False)

with tab2:
    st.header("AI Research Review")

    if st.button("Generate AI Review"):
        if not api_key:
            st.warning("Please enter your Groq API key.")
        else:
            try:
                client = Groq(api_key=api_key)

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a research methodology reviewer. "
                                "Evaluate the proposal critically. "
                                "Identify strengths, limitations and "
                                "practical recommendations. Do not invent "
                                "evidence or claim validation."
                            )
                        },
                        {
                            "role": "user",
                            "content": json.dumps(proposal_data)
                        }
                    ],
                    temperature=0.2
                )

                st.markdown(response.choices[0].message.content)

            except Exception as e:
                st.error(f"AI review error: {e}")

with tab3:
    st.header("Methodological Gap Prioritization")

    if st.button("Prioritize Research Gaps"):
        if not api_key:
            st.warning("Please enter your Groq API key.")
        else:
            try:
                client = Groq(api_key=api_key)

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Prioritize methodological gaps as Critical, "
                                "Important, or Optional. Explain why each "
                                "matters. Do not label already-defined items "
                                "as missing. Distinguish issues requiring "
                                "actual patient data from protocol decisions."
                            )
                        },
                        {
                            "role": "user",
                            "content": json.dumps(proposal_data)
                        }
                    ],
                    temperature=0.2
                )

                st.markdown(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Prioritization error: {e}")
