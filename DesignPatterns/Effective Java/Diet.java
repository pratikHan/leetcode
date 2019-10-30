public class Diet {

    private final int servings;
    private final int calories;
    private final int sodium;
    private final int calcium;


    public static class Builder{

        private final int servings;
        private final int calories;

        private int sodium;
        private int calcium;


        public Builder(int servings, int calories){

            this.servings = servings;
            this.calories = calories;

        }

        public Builder sodium(int sodium){
            this.sodium = sodium;
            return this;
        }

        public Builder calcium(int calcium){
               this.calcium = calcium;
               return this;
        }

        public Diet build(Builder builder){
               return new Diet(this);
         }
    }

        private Diet(Builder builder){

            this.servings = builder.servings;
            this.calories = builder.calories;
            this.sodium = builder.sodium;
            this.calcium = builder.calcium;



         }

}