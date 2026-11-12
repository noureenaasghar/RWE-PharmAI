
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

    st.title(proposal_data["Title"])

    st.subheader("Research Question")
    st.write(proposal_data["Research Question"])

    st.divider()

    st.subheader("Study Design")
    st.write(proposal_data["Study Design"])

    st.subheader("Target Population")
    population = proposal_data["Target Population"]

    st.write("Age:", population["age"])
    st.write("Required conditions:", ", ".join(population["required_conditions"]))
    st.write("Exposure group:", population["exposure_group"]["medication"])
    st.write("Comparator group:", population["comparator_group"]["medication"])
    st.write("Washout period:", population["washout_period"])
    st.write("Index date:", population["index_date"])

    st.divider()

    st.subheader("Eligibility Criteria")

    st.markdown("**Inclusion Criteria**")
    for item in proposal_data["Eligibility"]["Inclusion"]:
        st.markdown(f"- {item}")

    st.markdown("**Exclusion Criteria**")
    for item in proposal_data["Eligibility"]["Exclusion"]:
        st.markdown(f"- {item}")


    st.divider()

    st.subheader("Exposure and Comparator")

    st.markdown("**Exposure Group: GLP-1 Receptor Agonist Users**")
    exposure = proposal_data["Exposure"]

    st.markdown("- **Study population:** New users of GLP-1 receptor agonists")
    st.markdown("- **Medication evidence:** Prescription records; dispensing records, if available")
    st.markdown("- **Index date:** First eligible medication initiation")
    st.markdown("- **Comparator:** New users of DPP-4 inhibitors")
    st.info("Limitation: Prescription or dispensing records do not confirm actual medication use.")

    st.markdown("**Comparator Group: DPP-4 Inhibitor Users**")
    comparator = proposal_data["Comparator"]

    st.markdown(f"- **Population:** {comparator['population']}")
    st.markdown(f"- **Medication:** {comparator['medication']}")
    st.markdown(f"- **Design:** {comparator['design']}")
    st.markdown(f"- **Index date:** {comparator['index_date']}")
    st.markdown(f"- **Washout:** {comparator['washout']}")

    st.divider()

    st.subheader("Primary Outcomes")

    for name, details in proposal_data["Primary Outcomes"].items():
        st.markdown(f"**{name.replace('_', ' ')}**")
        for key, value in details.items():
            st.markdown(f"- **{key.replace('_', ' ').title()}:** {value}")

    st.divider()

    st.subheader("Statistical Analysis")

    analysis = proposal_data["Statistical Analysis"]

    st.markdown("**Descriptive Analysis**")
    for item in analysis["descriptive_analysis"]:
        st.markdown(f"- {item}")

    st.markdown("**Primary Analysis: Binary Outcomes**")
    primary = analysis["primary_analysis"]
    st.markdown("- **Statistical method:** Modified Poisson regression with robust standard errors")
    st.markdown("- **Effect measure:** Adjusted Risk Ratio (aRR)")
    st.markdown("- **Uncertainty:** 95% Confidence Interval")

    st.markdown("**Secondary Analysis: Recurrent Events**")
    secondary = analysis["secondary_analysis"]
    st.markdown("- **Statistical method:** Negative binomial regression, if overdispersion is present")
    st.markdown("- **Effect measure:** Incidence Rate Ratio (IRR)")
    st.markdown("- **Uncertainty:** 95% Confidence Interval")

    st.markdown("**Confounding Control**")
    for item in analysis["confounding_control"]:
        st.markdown(f"- {item}")

    st.markdown(f"**Significance level:** {analysis['significance_level']}")

    st.divider()

    st.subheader("Confounders")


    for category, variables in proposal_data["Confounders"].items():
        st.markdown(f"**{category.replace('_', ' ').title()}**")
        st.write(", ".join(variables))

    st.divider()

    st.subheader("Pending Validation")

    pending = proposal_data["Pending Validation"]

    for category, items in pending.items():
        st.markdown(f"**{category.replace('_', ' ').title()}**")
        for item in items:
            st.markdown(f"- {item}")

with tab2:
    st.header("AI Research Review")

    if st.button("Generate AI Review"):
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
                temperature=0.2,
                max_completion_tokens=8192
            )

            st.markdown(response.choices[0].message.content)

            if response.choices[0].finish_reason == "length":
                st.warning("Response reached its output limit.")

        except Exception as e:
            st.error(f"AI review error: {e}")


with tab3:
    st.header("Methodological Gap Prioritization")

    if st.button("Prioritize Research Gaps"):
        try:
            client = Groq(api_key=api_key)

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                       "content": (
    "You are a critical research methodology reviewer. "
    "Evaluate the proposal and prioritize methodological "
    "gaps using the following rules:\n\n"

    "1. Carefully read the entire proposal before identifying gaps.\n"
    "2. Never label an item as missing if it is already specified "
    "in the proposal.\n"
    "3. Classify each item using one of these statuses:\n"
    "- Specified: Clearly defined in the proposal.\n"
    "- Specified — Requires Validation: Defined, but needs "
    "literature, expert, or data validation.\n"
    "- Not Yet Specified: Important methodological detail "
    "is genuinely absent.\n"
    "- Data-Dependent: Cannot be determined until actual "
    "dataset assessment.\n"
    "4. Distinguish protocol decisions from data-dependent issues.\n"
    "5. Assign priority as Critical, Important, or Optional "
    "only where appropriate.\n"
    "6. For every identified gap, explain why it matters "
    "and give a practical recommendation.\n"
    "7. Refer to the relevant proposal section or existing "
    "methodological decision.\n"
    "8. Do not recommend repeating decisions already made "
    "unless further justification or validation is needed.\n"
    "9. Do not invent patient data, research findings, "
    "or evidence.\n\n"

    "Present the results in a structured table with these columns:\n"
    "Priority | Methodological Issue | Current Status | "
    "Why It Matters | Required Action | Category\n\n"

                           "10. In the final summary, include only genuinely "
"unresolved methodological decisions as unresolved gaps. "
"Do not describe an already-specified decision as missing.\n"

"11. Present validation tasks separately from missing "
"protocol decisions. Validation requirements do not "
"automatically constitute methodological gaps.\n"

"12. Do not automatically classify every validation "
"requirement as Critical. Assign priority according to "
"its actual impact on study validity and feasibility.\n"

"13. Do not recommend PDC, multiple imputation, "
"zero-inflated models, or other advanced methods as "
"mandatory. Recommend them only when the required data "
"and methodological justification are available.\n"

"14. Do not assume that the proposed 12-month washout "
"or follow-up period is inadequate. Identify these as "
"specified design choices requiring justification "
"or validation where appropriate.\n"
    "End with a concise summary of genuinely unresolved "
    "critical issues."
)
                    },
                    {
                        "role": "user",
                        "content": json.dumps(proposal_data)
                    }
                ],
                temperature=0.2,
                max_completion_tokens=8192
            )

            st.markdown(response.choices[0].message.content)

            if response.choices[0].finish_reason == "length":
                st.warning("Response reached its output limit.")

        except Exception as e:
            st.error(f"Prioritization error: {e}")
