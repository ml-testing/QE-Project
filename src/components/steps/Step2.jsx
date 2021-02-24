import React from 'react';
import { useForm } from 'react-hook-form';
import FormInput from '../FormInput';

const Step2 = ({ onSubmit }) => {
  const { register, handleSubmit, errors } = useForm();

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <h1>Step 2</h1>

        <FormInput id='firstName' label='First name' ref={register({ required: true })} errors={errors} />

        <FormInput id='lastName' label='Last name' ref={register({ required: true })} errors={errors} />

        <button type='submit' className='btn btn-primary' data-test-id='submit'>Next</button>

      </form>
    </div>
  );
}

export default Step2;
