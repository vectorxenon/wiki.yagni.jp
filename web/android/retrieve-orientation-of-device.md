# 端末の傾きを取得する

## 2.1以前

```java
class FooActivity extends Activity implements SensorEventListener
{
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        SensorManager.registerListener(this, SensorManager.getSensorList(Sensor.TYPE_ORIENTATION).get(0), SensorManager.Sensor_DELAY_NORMAL);
    }

    @Override
    public void onSensorChanged(SensorEvent event)
    {
        if (event.sensor.getType() == Sensor.TYPE_ORIENTATION) {
            float azimuth = event.values[0];
            float pitch = event.values[1];
            float roll = event.values[2];
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy)
    {
    }
}
```

## 2.2以降

_Sensor.TYPE_ORIENTATION_が非推奨になり、_SensorManager.getOrientation()_を使うようになった。

```java
class FooActivity extends Activity implements SensorEventListener
{
    SensorManager mSensorManager;
    boolean mSensorRegistered = false;
    Axis mOrientationAxis, mMagneticAxis, mAccelerometerAxis;

    static final int VECTOR_SIZE = 16;
    static final int ORIENTATION_MATRIX_SIZE = 3;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        mOrientationAxis = new Axis();
        mSensorManager = (SensorManager)getSystemService(Context.SENSOR_SERVICE);
    }

    @Override
    protected void onResume()
    {
        for (Sensor sensor: mSensorManager.getSensorList(Sensor.TYPE_ALL)) {
            switch (sensor.getType()) {
            case Sensor.TYPE_MAGNETIC_FIELD:
            case Sensor.TYPE_ACCELEROMETER:
                mSensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_UI);
                mSensorRegistered = true;
                break;
            default:
                break;
            }
        }
    }

    @Override
    protected void onPause()
    {
        if (mSensorRegistered) {
            mSensorManager.unregisterListener(this);
            mSensorRegistered = false;
        }
    }

    @Override
    public void onSensorChanged(SensorEvent event)
    {
        if (event.accuracy == SensorManager.SENSOR_STATUS_UNRELIABLE) {
            return;
        }
        switch (event.sensor.getType()) {
        case Sensor.TYPE_ACCELEROMETER:
            mAccelerometerAxis = new Axis(event.values);
            break;
        case Sensor.TYPE_MAGNETIC_FIELD:
            mMagneticAxis = new Axis(event.values);
            break;
        }
        if (mAccelerometerAxis != null && mMagneticAxis != null) {
            float[] inR = new float[VECTOR_SIZE];
            if (SensorManager.getRotationMatrix(inR, null, mAccelerometerAxis.toFloatArray(), mMagneticAxis.toFloatArray())) {
                float[] outR = new float[VECTOR_SIZE];
                switch (getResources().getConfiguration().orientation) {
                case Configuration.ORIENTATION_LANDSCAPE:
                    SensorManager.remapCoordinateSystem(inR, SensorManager.AXIS_Y, SensorManager.AXIS_MINUS_X, outR);
                    break;
                case Configuration.ORIENTATION_PORTRAIT:
                    SensorManager.remapCoordinateSystem(inR, SensorManager.AXIS_X, SensorManager.AXIS_Z, outR);
                    break;
                default:
                    return;
                }
                mOrientationAxis = new Axis(SensorManager.getOrientation(outR, mOrientationAxis.toFloatArray()));
                Log.d(TAG, mOrientationAxis.toString());
            }
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy)
    {
    }

    class Axis
    {
        private float[] values;
        /**
         * rotation around the Z axis.
         */
        public float azimuth;

        /**
         * rotation around the X axis.
         */
        public float pitch;

        /**
         * rotation around the Y axis.
         */
        public float roll;

        public Axis()
        {
            values = new float[ORIENTATION_MATRIX_SIZE];
        }

        public Axis(float[] values) throws RuntimeException
        {
            if (values.length < 3) {
                throw new RuntimeException("Axis constructor's argument need tree elements.");
            }
            this.values = values.clone();
            azimuth = values[0];
            pitch = values[1];
            roll = values[2];
        }

        public float[] toFloatArray()
        {
            return values;
        }

        @Override
        public String toString()
        {
            return String.valueOf(Math.toDegrees(pitch)) + "," +
                String.valueOf(Math.toDegrees(roll)) + "," +
                String.valueOf(Math.toDegrees(azimuth));
        }
    }
}
```
