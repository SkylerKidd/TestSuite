/**
 * Created by norelltagle on 5/10/16.
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class UITestCase {
    private int family_income_exclusion;
    private int family_income_contribution;
    private int percent_disc_income_saved;
    private int years_of_saving;
    private int interest_on_savings;
    private int hours_worked;
    private int tuition_adjustment;
    private String totalCost;

    public UITestCase() {

    }

    public UITestCase(int family_income_exclusion, int family_income_contribution, int percent_disc_income_saved, int years_of_saving, int interest_on_savings, int hours_worked, int tuition_adjustment, String totalCost) {
        this.family_income_exclusion = family_income_exclusion;
        this.family_income_contribution = family_income_contribution;
        this.percent_disc_income_saved = percent_disc_income_saved;
        this.years_of_saving = years_of_saving;
        this.interest_on_savings = interest_on_savings;
        this.hours_worked = hours_worked;
        this.tuition_adjustment = tuition_adjustment;
        this.totalCost = totalCost;
    }


    public int getFamily_income_exclusion() {
        return family_income_exclusion;
    }

    public String getTotalCost() {
        return totalCost;
    }

    public void setTotalCost(String totalCost) {
        this.totalCost = totalCost;
    }

    public void setFamily_income_exclusion(int family_income_exclusion) {
        this.family_income_exclusion = family_income_exclusion;
    }

    public int getFamily_income_contribution() {
        return family_income_contribution;
    }

    public void setFamily_income_contribution(int family_income_contribution) {
        this.family_income_contribution = family_income_contribution;
    }

    public int getPercent_disc_income_saved() {
        return percent_disc_income_saved;
    }

    public void setPercent_disc_income_saved(int percent_disc_income_saved) {
        this.percent_disc_income_saved = percent_disc_income_saved;
    }

    public int getYears_of_saving() {
        return years_of_saving;
    }

    public void setYears_of_saving(int years_of_saving) {
        this.years_of_saving = years_of_saving;
    }

    public int getInterest_on_savings() {
        return interest_on_savings;
    }

    public void setInterest_on_savings(int interest_on_savings) {
        this.interest_on_savings = interest_on_savings;
    }

    public int getHours_worked() {
        return hours_worked;
    }

    public void setHours_worked(int hours_worked) {
        this.hours_worked = hours_worked;
    }

    public int getTuition_adjustment() {
        return tuition_adjustment;
    }

    public void setTuition_adjustment(int tuition_adjustment) {
        this.tuition_adjustment = tuition_adjustment;
    }
}
