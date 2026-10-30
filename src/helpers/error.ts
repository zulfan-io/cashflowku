import { toast } from '~/stores/toast'
import { useLoading } from '~/stores/loading'

export const handleError = (error: any) => {
  const loading = useLoading()
  toast().updateToast('error', `${error.message}. Try again!`, true)
  loading.isLoading = false
  return (`Error message: ${error.message}`)
}
